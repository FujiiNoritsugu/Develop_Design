def main():
    for data in (temp for temp in (1, 2, 3, 4, 5)):
        print(data)
        if data > 2:
            break


if __name__ == '__main__':
    main()
