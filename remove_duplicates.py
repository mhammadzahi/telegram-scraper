import argparse


def main():
    parser = argparse.ArgumentParser(description='Lowercase and de-duplicate a list of emails.')
    parser.add_argument('input', help='Path to the file containing emails (one per line)')
    parser.add_argument('-o', '--output', help='Output file (default: overwrite input file)')
    args = parser.parse_args()

    output = args.output or args.input

    with open(args.input, 'r') as f:
        emails = [line.strip().lower() for line in f if line.strip()]

    unique_emails = list(dict.fromkeys(emails))

    with open(output, 'w') as f:
        for email in unique_emails:
            f.write(email + '\n')

    print(f'{len(emails)} emails -> {len(unique_emails)} unique. Written to {output}')


if __name__ == '__main__':
    main()
