import requests
import hashlib
import sys

#This function is essential for fetching the list of hash suffixes from the "Have I Been Pwned" API, which is then used to check if a specific password has been compromised.
def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}, check the api and try again') 
    return res 

def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0

def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()  # converting the input password into a SHA-1 hash and formatting it in a way that is compatible with the "Have I Been Pwned" API.
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char) #returns data for all suffixes corresponding to this prefix.
    return get_password_leaks_count(response, tail)

def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f'{password} was found {count} times... you should probably change your password!')
        else:
            print(f'{password} was NOT found. Carry on with this password!')
    return 'done!'

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))