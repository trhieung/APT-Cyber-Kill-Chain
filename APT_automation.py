import os
import subprocess
import csv
from dotenv import load_dotenv
from tools/gophish/custom_gophish import custom_gophish

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

        try:
            # Run the shell script with the collected parameters
            subprocess.run(["bash", script_path, "-d", domain, "-o", output_file, "-r", output_directory], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            print("Shell script executed successfully.")

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

class weaponization:
    def __init__(self) -> None:
        print(self)
    
    def __str__(self) -> str:
        return (
            "WEAPONIZATION PHASE:\n"
            "---------------------------------------\n"
            "Generate payload with Sliver in ps1 format\n"
            "Upload to Apache server\n"
        )

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

class installation:
    def __init__(self) -> None:
        print(self)

    def __str__(self) -> str:
        return (
            "INSTALLATION PHASE:\n"
            "---------------------------------------\n"
            "Waiting for target systems running the payload for creating the backdoor ...\n"
        )

def main():
    list_phase = []
    list_phase.append(reconaissance())
    list_phase.append(weaponization())
    list_phase.append(delivery())
    list_phase.append(installation())

if __name__ == '__main__':
    main()

    # finish automation for
    print("nice to meet you!")