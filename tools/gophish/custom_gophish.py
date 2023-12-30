from gophish import Gophish
from gophish.models import *
import random
import string
import os
from dotenv import load_dotenv
import csv
import ast
import base64
import mimetypes


def random_string(length):
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string

# Attachmment missing init function
class Attachment(Attachment):
    def __init__(self, **kwargs):
        for key, default in User._valid_properties.items():
            setattr(self, key, kwargs.get(key, default))

class custom_gophish():
    def __init__(self, api_key="eba531afc28a392f0b5e36de14c08a7ee025d97e96b43a744eccc2511f04995c", 
                host = 'https://127.0.0.1:3333') -> None:
        
        self.api = Gophish(api_key=api_key, host=host, verify=False)
        load_dotenv()
        

    def group_new(self, name=random_string(10)):
        def read_csv(path_to_csv):
            users = []
            with open(path_to_csv, 'r') as csv_file:
                reader = csv.DictReader(csv_file)
                for row in reader:
                    lowercase_row = {key.lower(): value for key, value in row.items()}
                    user = User(**lowercase_row)
                    users.append(user)
            return users
        
        def handle_file_name():
            pass

        # next update need to check if exist group_name

        emails = ast.literal_eval(os.getenv('EMAILS_FILE'))
        file_names = [os.path.join(os.getenv('PATH_EMAILS'), name) for name in emails]

        targets = []
        for file_name in file_names:
            targets.extend(read_csv(file_name))
        
        group = Group(name=name, targets=targets)
        group = self.api.groups.post(group)

        return (group.name, group.id)

    def template_new(self, name=random_string(10)):
        def get_content(path_to_payload):
            with open(path_to_payload, 'rb') as bin_read:
                b64_attachment_content = base64.b64encode(bin_read.read())

            return b64_attachment_content

        payloads = ast.literal_eval(os.getenv('PAYLOADS_FILE'))
        targets = [Attachment.parse(
            {   
                'content': get_content(os.path.join(os.getenv('PATH_PAYLOADS'), payload)).decode(),
                'type': mimetypes.guess_type(payload)[0],
                'name': payload
            }
        ) for payload in payloads]
        
        html = os.path.join(os.getenv('PATH_TEMPLATES'), os.getenv('HTML_FILE_FOR_TEMPLATE'))
        with open(html, 'r') as file:
            html_content = file.read()

        template = Template(name=name,
                            html=html_content,
                            attachments=targets)

        template = self.api.templates.post(template)
        return (template.name, template.id)
        
    def page_new(self, name=random_string(10)):
        
        html = os.path.join(os.getenv('PATH_PAGES'), os.getenv('HTML_FILE_FOR_PAGE'))
        with open(html, 'r') as file:
            html_content = file.read()

        page = Page(name=name,
                    html=html_content)

        page = self.api.pages.post(page)

        return (page.name, page.id)

    def profile_new(self, name=random_string(10)):
        username = os.getenv("SEND_MAIL_USERNAME")
        password = os.getenv("SEND_MAIL_PASSWORD")
        smtp = SMTP(interface_type = "SMTP",
                    name=name, 
                    host=os.getenv("SMTP_HOST"),
                    username=username,
                    password=password,
                    from_address = f"{username}",
                    ignore_cert_errors = True)

        smtp = self.api.smtp.post(smtp)
        return (smtp.name, smtp.id)

    def campaign_new(self, name=random_string(10)):
        
        groups = [Group(name=self.group_new()[0])]
        page = Page(name=self.page_new()[0])
        template = Template(name=self.template_new()[0])
        smtp = SMTP(name=self.profile_new()[0])

        campaign = Campaign(name=name, 
                            groups=groups, 
                            page=page,
                            template=template, 
                            smtp=smtp,
                            url=os.getenv('CC_SERVER'))

        campaign = self.api.campaigns.post(campaign)
        print(campaign.name, campaign.id)

    def group_delete_all(self):
        for group in self.api.groups.get():
            self.api.groups.delete(group.id)

    def template_delete_all(self):
        for template in self.api.templates.get():
            self.api.templates.delete(template.id)
        
    def page_delete_all(self):
        for page in self.api.pages.get():
            self.api.pages.delete(page.id)
            
    def profile_delete_all(self):
        for profile in self.api.smtp.get():
            self.api.smtp.delete(profile.id)

    def campaign_delete_all(self):
        for campaign in self.api.campaigns.get():
            self.api.campaigns.delete(campaign.id)

    def delete_all(self):
        self.campaign_delete_all()
        self.group_delete_all()
        self.template_delete_all()
        self.page_delete_all()
        self.profile_delete_all()

# mygophish = custom_gophish()
# mygophish.group_new()
# mygophish.template_new()
# mygophish.page_new()
# mygophish.profile_new()
# mygophish.campaign_new()
# mygophish.delete_all()