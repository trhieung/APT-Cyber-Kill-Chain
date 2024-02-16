import os
import subprocess
from dotenv import load_dotenv

def run_shell_script(script_path):
    try:
        # Run the shell script
        subprocess.run(["bash", script_path], check=True)
        print("Shell script executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error executing shell script: {e}")

class reconaissance:
    def __init__(self) -> None:
        self.web_domain = ""

        load_dotenv()
        self.get_web_domain()
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
    
    def get_web_domain(self):
        self.web_domain = os.getenv("WEB_DOMAIN")

    def start_spiderfoot(self):
        # Provide the path to your shell script
        script_path = "test_spiderfoot.sh"

        # Call the function to run the shell script
        run_shell_script(script_path)

def main():
    list_phase = []
    list_phase.append(reconaissance())
    a = list_phase[0]
    print(a)

if __name__ == '__main__':
    main()

    # finish automation for
    print("nice to meet you!")