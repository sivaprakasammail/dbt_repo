import os

if __name__ == "__main__":
  with open('google-key.json', 'w') as f:
    f.write(os.environ['DBT_USER_JSON'])
