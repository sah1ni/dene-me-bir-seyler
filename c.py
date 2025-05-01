start = int(input("Nereden başlasın?: "))
end = int(input("Nereye kadar olsun?: "))

x = list(range(start, end + 1))
print(*x, sep=", ")
