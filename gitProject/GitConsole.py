import subprocess


def set_git_email(email, global_scope=False):
    try:
        # Determine the scope of the setting (global or local)
        scope = "--global" if global_scope else "--local"

        # Check if user.email is already set
        try:
            current_email = subprocess.run(
                ["git", "config", "--get", scope, "user.email"],
                check=True,
                capture_output=True,
                text=True
            )
            print(f"Current Git user email: {current_email.stdout.strip()}")

            # Unset the existing user.email
            subprocess.run(["git", "config", "--unset", scope, "user.email"], check=True)
            print("Previous Git user email configuration has been removed.")

        except subprocess.CalledProcessError:
            print("No existing Git user email configuration found.")

        # Execute the git command to set the new user email
        subprocess.run(["git", "config", scope, "user.email", email], check=True)

        # Verify the change
        result = subprocess.run(["git", "config", scope, "user.email"], check=True, capture_output=True, text=True)
        print(f"Git user email has been set to: {result.stdout.strip()}")

    except subprocess.CalledProcessError as e:
        print(f"An error occurred while setting the Git user email: {e}")


def set_git_username(username, global_scope=False):
    try:
        # Determine the scope of the setting (global or local)
        scope = "--global" if global_scope else "--local"

        # Check if user.email is already set
        try:
            current_username = subprocess.run(
                ["git", "config", "--get", scope, "user.name"],
                check=True,
                capture_output=True,
                text=True
            )
            print(f"Current Git user name: {current_username.stdout.strip()}")

            # Unset the existing user.email
            subprocess.run(["git", "config", "--unset", scope, "user.name"], check=True)
            print("Previous Git user name configuration has been removed.")

        except subprocess.CalledProcessError:
            print("No existing Git user name configuration found.")

        # Execute the git command to set the new user email
        subprocess.run(["git", "config", scope, "user.name", username], check=True)

        # Verify the change
        result = subprocess.run(["git", "config", scope, "user.name"], check=True, capture_output=True, text=True)
        print(f"Git user name has been set to: {result.stdout.strip()}")

    except subprocess.CalledProcessError as e:
        print(f"An error occurred while setting the Git user name: {e}")

def set_git_userpassword(userpassword, global_scope=False):
    try:
        # Determine the scope of the setting (global or local)
        scope = "--global" if global_scope else "--local"

        # Check if user.email is already set
        try:
            current_userpassword = subprocess.run(
                ["git", "config", "--get", scope, "user.password"],
                check=True,
                capture_output=True,
                text=True
            )
            print(f"Current Git user password: {current_userpassword.stdout.strip()}")

            # Unset the existing user.email
            subprocess.run(["git", "config", "--unset", scope, "user.password"], check=True)
            print("Previous Git user password configuration has been removed.")

        except subprocess.CalledProcessError:
            print("No existing Git user password configuration found.")

        # Execute the git command to set the new user email
        subprocess.run(["git", "config", scope, "user.password", userpassword], check=True)

        # Verify the change
        result = subprocess.run(["git", "config", scope, "user.password"], check=True, capture_output=True, text=True)
        print(f"Git user password has been set to: {result.stdout.strip()}")

    except subprocess.CalledProcessError as e:
        print(f"An error occurred while setting the Git user password: {e}")


if __name__ == "__main__":

    email_to_set = input("Please enter the email address you want to set: ")
    userName_to_set=input("Please enter the username you want to set: ")
    userPasssword_to_set = input("Please enter the userpassword you want to set: ")

    scope_input = input("Do you want to set the email globally? (yes/no): ").strip().lower()
    global_scope = scope_input == 'yes'

    set_git_email(email_to_set, global_scope=global_scope)
    set_git_username(userName_to_set, global_scope=global_scope)
    set_git_userpassword(userPasssword_to_set, global_scope=global_scope)