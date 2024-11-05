#!/usr/local/autopkg/python

import json
from autopkglib import ProcessorError, URLGetter

__all__ = ["QualysCloudAgentURLProvider"]

class QualysCloudAgentURLProvider(URLGetter):

    description = __doc__
    input_variables = {
        "qualys_api_url": {
            "required": True,
            "default": "https://qualysapi.qualys.com",
            "description": (
                "Qualys maintains multiple Qualys Cloud Platforms.",
                "The API server URL that you should use for API requests",
                "depends on the platform where your Qualys account is located."
            ),
        },
        "qualys_username": {
        	"required": True,
        	"description": (
        		"Qualys Cloud Agent API Username.",
        		"This account requires the Access Permission \"API Access\" and",
        		"Asset Management Permission \"Read Asset\" in the Qualys console"
        },
        "qualys_password": {
            "required": True,
            "description": "Qualys Cloud Agent API Password"
        },
        "qualys_arch": {
        	"required": True,
        	"description": "Architecture of the PKG to download. Either arm64 or x64."
    }
    output_variables = {
        "qualys_url": {"description": "Returns the url to download."},
        "qualys_version": {"description": "Returns the version and architecture of the package to download."},
    }

    def main(self):
    
    	# API Variables
		qualys_api_url = self.env.get("qualys_api_url")
		qualys_username = self.env.get("qualys_username")
		qualys_password = self.env.get("qualys_password")

#    def main(self):
#
#        # Define variables
#        qualys_username = self.env.get("qualys_username")
#        qualys_password = self.env.get("qualys_password")
#        qualys_api_server = self.env.get("qualys_api_server")
#
#        token_url = f"{api_region_url}/oauth2/token"
#        policy_url = f"{api_region_url}/policy/combined/sensor-update/v1?filter=platform_name%3A'Mac'"
#        installer_url = f"{api_region_url}/sensors/combined/installers/v1?filter=platform%3A%22mac%22"
#
#        # Verify the input variables were provided
#        if not client_id or client_id == "%CLIENT_ID%":
#            raise ProcessorError("The input variable 'client_id' was not set!")
#        if not client_secret or client_secret == "%CLIENT_SECRET%":
#            raise ProcessorError("The input variable 'client_secret' was not set!")
#        if not policy_id or policy_id == "%POLICY_ID%":
#            raise ProcessorError("The input variable 'policy_id' was not set!")
#
#        # Build the headers
#        headers = {
#            "accept": "application/json",
#            "Content-Type": "application/x-www-form-urlencoded",
#        }
#
#        # Build the required curl switches
#        curl_opts = [
#            "--url",
#            f"{token_url}",
#            "--request",
#            "POST",
#            "--data",
#            f"client_id={client_id}&client_secret={client_secret}"
#        ]
#
#        try:
#            # Initialize the curl_cmd, add the curl options, and execute curl
#            curl_cmd = self.prepare_curl_cmd()
#            self.add_curl_headers(curl_cmd, headers)
#            curl_cmd.extend(curl_opts)
#            response_token = self.download_with_curl(curl_cmd)
#
#        except:
#            raise ProcessorError("Failed to authenticate with the QualysCloudAgent API!")
#
#        try:
#            # Load the JSON response
#            json_data = json.loads(response_token)
#            access_token = json_data["access_token"]
#            self.output(f"Access Token:  {access_token}", verbose_level=3)
#
#        except:
#            raise ProcessorError("Failed to acquire the bearer authentication token!")
#
#        try:
#
#            auth_headers = {
#                "accept": "application/json",
#                "authorization": f"bearer {access_token}",
#            }
#
#            # Execute curl
#            response_policies = self.download(url=policy_url, headers=auth_headers)
#
#            # Load the JSON response
#            json_data = json.loads(response_policies)
#
#        except:
#            raise ProcessorError("Failed to get the Sensor Update Policies!")
#
#        try:
#
#            # Loop through the policies to find the desired policy id
#            for policy in json_data["resources"]:
#
#                if policy.get("id") == policy_id:
#
#                    # Get the build assigned to the policy
#                    build = policy.get("settings")["build"]
#
#            build_version = build.split("|", 1)[0]
#            self.output(
#                f"Build version for matching Policy:  {build_version}", verbose_level=1)
#
#        except:
#            raise ProcessorError("Failed to match a Sensor Update Policy!")
#
#        try:
#            # Execute curl
#            response_installers = self.download(url=installer_url, headers=auth_headers)
#
#            # Load the JSON response
#            json_data = json.loads(response_installers)
#
#        except:
#            raise ProcessorError("Failed to acquire list of installers!")
#
#        try:
#            # Loop through the installers to to find the desired build
#            for installer in json_data["resources"]:
#
#                # The build is the last string of digits of the version string
#                if installer.get("version").split(".")[-1] == build_version:
#                    version = installer.get("version")
#                    sha256 = installer.get("sha256")
#
#        except:
#            raise ProcessorError(
#                "Failed to match an available sensor version to the Policy assigned build version!")
#
#        try:
#            download_url = f"{api_region_url}/sensors/entities/download-installer/v1?id={sha256}"
#
#            self.env["access_token"] = access_token
#            # This version is appended to match the _actual_ CFBundleShortVersionString
#            self.env["version"] = f"{version}.0"
#            self.env["download_url"] = download_url
#
#            self.output(
#                f"Sensor version that will be downloaded: {self.env['version']}", verbose_level=1)
#            self.output(f"Download URL:  {download_url}", verbose_level=3)
#
#        except:
#            raise ProcessorError("Something went wrong assigning environment variables!")


if __name__ == "__main__":
    processor = QualysCloudAgentURLProvider()
    processor.execute_shell()
