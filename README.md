
# Password Pwned Checker 🚨🔒

Welcome to the **Password Pwned Checker**! This Python script helps you find out if your passwords have been compromised in known data breaches using the "Have I Been Pwned" API. Keep your accounts secure by checking your passwords against this database of exposed credentials.

## 🚀 How It Works

1. **Hashing**:
   - The script converts your password into a SHA-1 hash.

2. **API Query**:
   - It sends a request to the "Have I Been Pwned" API with the first 5 characters of the hash.
   - The API returns a list of suffixes for this prefix along with their breach counts.

3. **Suffix Matching**:
   - The script checks if the suffix of your hash matches any in the API response.

4. **Result**:
   - It informs you if your password has been compromised and how many times.

## 🔍 Code Breakdown

### `request_api_data(query_char)`

Fetches data from the "Have I Been Pwned" API based on the hash prefix.

- **Parameters**: 
  - `query_char`: The first 5 characters of the SHA-1 hash.
- **Returns**: 
  - A `requests.Response` object with suffixes and counts.
- **Error Handling**:
  - Raises a `RuntimeError` if the API request fails (status code other than 200).

### `get_password_leaks_count(hashes, hash_to_check)`

Determines how many times a hash suffix has been exposed.

- **Parameters**:
  - `hashes`: API response with suffixes and counts.
  - `hash_to_check`: The suffix part of the SHA-1 hash.
- **Returns**:
  - The number of breaches for the suffix or 0 if not found.

### `pwned_api_check(password)`

Checks if a password has been compromised.

- **Parameters**:
  - `password`: The password to check.
- **Returns**:
  - The count of how many times the password was found or 0 if not found.
- **Steps**:
  - Computes SHA-1 hash.
  - Splits hash into prefix and suffix.
  - Queries the API with the prefix and checks the suffix.

### `main(args)`

The script’s main function, executed from the command line.

- **Parameters**:
  - `args`: List of passwords to check.
- **Prints**:
  - Whether each password was found in breaches and how many times or if it was not found.

## 🚀 Running the Script

To use the Password Pwned Checker, run the script with your passwords as command-line arguments:

```bash
python script_name.py yourpassword1 yourpassword2
```

Replace `script_name.py` with your Python script file name.

## 📦 Dependencies

- `requests`: For making HTTP requests.
- `hashlib`: For hashing passwords with SHA-1.

Install dependencies using pip:

```bash
pip install requests
```


---

**Stay secure and keep your passwords safe!** If you have any questions or need help, feel free to open an issue or contribute to the project. Happy coding! 🚀🔐

