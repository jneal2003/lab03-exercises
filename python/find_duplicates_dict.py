def find_duplicates_dict(l: list) -> list:
    seen = {}
    dupes = []
    for num in l:
        if num in seen and num not in dupes:
            seen[num] += 1
            dupes.append(num)
        else:
            seen[num] = 1
    return dupes

sample1 = [3, 7, 5, 6, 7, 4, 8, 5, 7, 66]
sample2 = [3, 5, 6, 4, 4, 5, 66, 6, 7, 6]
sample3 = [3, 0, 5, 1, 0]
sample4 = [3]
    
print("Sample 1:", find_duplicates_dict(sample1))
print("Sample 2:", find_duplicates_dict(sample2))
print("Sample 3:", find_duplicates_dict(sample3))
print("Sample 4:", find_duplicates_dict(sample4))
            
