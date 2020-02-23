import jpl

if __name__ == "__main__":
    client = jpl.JiggyPlaybookLint(path="examples/jiggy-playbook.yml")
    result = client.validate()
