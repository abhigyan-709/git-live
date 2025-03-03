def http_error(status):
    match status:
        case 400:
            return "Bad Request"
        case 200:
            return "Success"
        case 404:
            return "Page not found"
        

def main():
    status = int(input("Please write the status code : "))
    http_error(status)
    print(http_error(status))


if __name__ == "__main__":
    main()