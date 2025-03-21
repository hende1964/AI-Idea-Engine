import subprocess
import json
import shutil

# Locate Railway CLI automatically
RAILWAY_CLI_PATH = shutil.which("railway") or "C:\\Users\\scott\\AppData\\Roaming\\npm\\railway.cmd"

def get_projects():
    """Fetches all Railway projects and returns them as a list of dictionaries."""
    try:
        result = subprocess.run([RAILWAY_CLI_PATH, "projects", "--json"], capture_output=True, text=True, check=True)
        projects = json.loads(result.stdout)
        return projects
    except Exception as e:
        print(f"Error fetching projects: {e}")
        return []

def get_project_status(project_id):
    """Checks if a Railway project has any deployments."""
    try:
        result = subprocess.run([RAILWAY_CLI_PATH, "status", "-p", project_id], capture_output=True, text=True, check=True)
        return "No deployments found" in result.stdout
    except Exception as e:
        print(f"Error checking project status for {project_id}: {e}")
        return False

def delete_project(project_id, project_name):
    """Deletes a Railway project by ID."""
    try:
        subprocess.run([RAILWAY_CLI_PATH, "delete", "-p", project_id, "-y"], check=True)
        print(f"Deleted empty project: {project_name} ({project_id})")
    except Exception as e:
        print(f"Failed to delete project {project_name} ({project_id}): {e}")

def main():
    print("Fetching all Railway projects...")
    projects = get_projects()

    if not projects:
        print("No projects found.")
        return

    for project in projects:
        project_id = project.get("id")
        project_name = project.get("name")

        if get_project_status(project_id):
            delete_project(project_id, project_name)
        else:
            print(f"Project {project_name} ({project_id}) has deployments, skipping...")

    print("Cleanup complete!")

if __name__ == "__main__":
    main()


