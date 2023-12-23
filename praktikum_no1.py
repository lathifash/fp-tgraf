class SegmentTree:
    # Init
    def __init__(self, n):
        self.n = n
        # create segment tree
        # karena segment tree untuk array ukuran n adalah 2*n - 1 maka. jumlah nodenya adalah (2*n)
        self.tree = [0] * (2 * n)

    # update Tree
    def update(self, index, value):
        # adjust index
        index += self.n
        # update value nya
        self.tree[index] = value
        # update node parent parentnya dengan max dari child
        while index > 1:
            index //= 2
            self.tree[index] = max(self.tree[2 * index], self.tree[2 * index + 1])

    # cari max value dari range [left, right]
    def query(self, left, right):
        # adjust index
        left += self.n
        right += self.n
        result = 0

        # cek apakah left < right. traverse dari bawah (child) ke atas (parent)
        while left < right:
            # jika left merupakan child kanan
            if left % 2 == 1:
                # bandingkan dengan result
                result = max(result, self.tree[left])
                left += 1

            # jika right merupakan child kanan
            if right % 2 == 1:
                right -= 1
                # bandingkan dengan result
                result = max(result, self.tree[right])

            # ke node parent
            left //= 2
            right //= 2

        return result


def longest_increasing_subsequence(nums):
    n = len(nums)

    # map index : sorted num
    index_map = {num: i for i, num in enumerate(sorted(set(nums)))}

    # buat segment tree
    segment_tree = SegmentTree(len(index_map))

    # track panjang lis
    lis_length = 0
    ending_index = 0  # Menyimpan indeks terakhir dari LIS

    # iterates tiap nums
    for num in nums:
        # ambil index dari hasil map
        index = index_map[num]

        # gunakan segment tree untuk mendapatkan max length increasing subsequence yang berakhiran index
        # + 1 untuk menghitung nums saat ini juga
        length = segment_tree.query(0, index) + 1

        # update segment tree dengan length baru index
        segment_tree.update(index, length)

        # bandingkan dengan lis_length
        if length > lis_length:
            lis_length = length
            ending_index = index

    # Rekonstruksi LIS
    lis = []
    for i in range(lis_length - 1, -1, -1):
        # Menggunakan index_map_reverse untuk mendapatkan kembali elemen sebenarnya dari indeks
        lis.append(list(index_map.keys())[list(index_map.values()).index(ending_index)])
        ending_index -= 1

    return lis[::-1], lis_length

# Driver Code
nums = [4, 1, 13, 7, 0, 2, 8, 11, 3]
result, length = longest_increasing_subsequence(nums)

print("Panjang LIS:", length)
print("Salah satu solusi:", result)
