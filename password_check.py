import sys

def get_list_of_passwords(filename):
    ret = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            ret.append(line.strip())
    return ret

def main(word, password_filename = '1000-most-common-passwords.txt'):
    # Get list of most commonly-used passwords
    passwords = get_list_of_passwords(password_filename)
    
    if word in passwords:
        return True
    return False

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python3 password_check.py [password]')
        sys.exit()

    result = main(sys.argv[1])
    if result:
        print('Common password')
    else:
        print('Not common password')
