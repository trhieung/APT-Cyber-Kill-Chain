import os
import subprocess
from dotenv import load_dotenv

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
        # self.start_spiderfoot()

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

    def run_shell_script_with_env(script_path):
        # Load environment variables from .env file
        load_dotenv()

        # Collect parameters from environment variables
        domain = os.getenv("WEB_DOMAIN")
        output_file = os.getenv("EMAIL_FILE")
        output_directory = os.getenv("PATH_EMAILS")

        try:
            # Run the shell script with the collected parameters
            subprocess.run(["bash", script_path, "-d", domain, "-o", output_file, "-r", output_directory], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            print("Shell script executed successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Error executing shell script: {e}")

    def start_spiderfoot(self):
        # Provide the path to your shell script
        script_path = "test_spiderfoot.sh"

        # Call the function to run the shell script
        run_shell_script(script_path)

def main():
    list_phase = []
    list_phase.append(reconaissance())
    # a = list_phase[0]
    # print(a)

if __name__ == '__main__':
    main()

    # finish automation for
    print("nice to meet you!")