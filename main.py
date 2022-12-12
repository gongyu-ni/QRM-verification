# QRM(1,4)
#  |0> ⊗ (α|0> + β|1>) ⊗ [|0>⊗[(|0>+|1>)/sqrt(2)]]^⊗6 ⊗|0>
# quantum circuit: 6 hadamard gate and 6 |0> state and 1 arbitary input
# combination of state seed state α:|0000 0000 0000 000> β:|0101 0101 0101 010>
# calculation of all α state 000 _0_0_0_0_0_0
# calculation of all β state 010 _0_0_0_0_0_0

# here we first all combinations of _0_0_0_0_0_0 where _ can be input 0 or 1, there are 6 _ in total
# get 2^6 combination of 0 and 1
# for i in range(64):
#     print(bin(i))

# read these date from file
# opening the file in read mode
my_file = open("bin_for_6.txt", "r")
# read lines
content_list = my_file.readlines()

my_file.close()

# print(content_list)

# convert content_list str to list
convert_list = []

for i in range(64):
    a = list(map(int, content_list[i].split()))
    convert_list.append(a)

# print(convert_list)

# combine with 0 in the form : _0_0_0_0_0_0
# 12 bit list
contain_12_bits = []
list_contain_12_bits = []

for i in range(len(convert_list)):
    for j in convert_list[i]:
        contain_12_bits.append(j)
        contain_12_bits.append(0)

    list_contain_12_bits.append(list(contain_12_bits))
    contain_12_bits.clear()

# print(list_contain_12_bits)

# add 000 in the front to get all α state , denote as "a"
list_contain_15_bits_a = []
list_contain_15_a = [0, 0, 0]

for i in range(len(list_contain_12_bits)):
    for j in list_contain_12_bits[i]:
        list_contain_15_a.append(j)
    list_contain_15_bits_a.append(list(list_contain_15_a))
    list_contain_15_a = [0, 0, 0]

# print(list_contain_15_bits_a)

# add 010 in the front to get all β state , denote as "b"
list_contain_15_bits_b = []
list_contain_15_b = [0, 1, 0]

for i in range(len(list_contain_12_bits)):
    for j in list_contain_12_bits[i]:
        list_contain_15_b.append(j)
    list_contain_15_bits_b.append(list(list_contain_15_b))
    list_contain_15_b = [0, 1, 0]

# print(list_contain_15_bits_b)

# reverse the order of all β state (means to put |0101 0101 0101 010> in the first place)
list_contain_15_bits_b_r = []
element_in_b = len(list_contain_15_bits_b) - 1

while element_in_b >= 0:
    list_contain_15_bits_b_r.append(list_contain_15_bits_b[element_in_b])
    element_in_b = element_in_b - 1

# print(list_contain_15_bits_b_r)

# x stabilizer
stabilizer_list = [0b000000011111111, 0b000111100001111, 0b011001100110011, 0b101010101010101]

# for α state, we need to convert list_contain_15_bits_a into integer components

# for i in range(len(list_contain_15_bits_a)):
#     s = [str(integer) for integer in list_contain_15_bits_a[i]]
#     a_string = "".join(s)
#     res = int(a_string)
#     print(res)
bit_list_r = [0b000000000000000, 0b000000000000010, 0b000000000001000, 0b000000000001010, 0b000000000100000,
              0b000000000100010, 0b000000000101000
    , 0b000000000101010, 0b000000010000000, 0b000000010000010, 0b000000010001000, 0b000000010001010, 0b000000010100000,
              0b000000010100010
    , 0b000000010101000, 0b000000010101010, 0b000001000000000, 0b000001000000010, 0b000001000001000, 0b000001000001010,
              0b000001000100000
    , 0b000001000100010, 0b000001000101000, 0b000001000101010, 0b000001010000000, 0b000001010000010, 0b000001010001000,
              0b000001010001010
    , 0b000001010100000, 0b000001010100010, 0b000001010101000, 0b000001010101010, 0b000100000000000, 0b000100000000010,
              0b000100000001000
    , 0b000100000001010, 0b000100000100000, 0b000100000100010, 0b000100000101000, 0b000100000101010, 0b000100010000000,
              0b000100010000010
    , 0b000100010001000, 0b000100010001010, 0b000100010100000, 0b000100010100010, 0b000100010101000, 0b000100010101010,
              0b000101000000000
    , 0b000101000000010, 0b000101000001000, 0b000101000001010, 0b000101000100000, 0b000101000100010, 0b000101000101000,
              0b000101000101010
    , 0b000101010000000, 0b000101010000010, 0b000101010001000, 0b000101010001010, 0b000101010100000, 0b000101010100010,
              0b000101010101000
    , 0b000101010101010, 0b000000000000000, 0b000000000000010, 0b000000000001000, 0b000000000001010, 0b000000000100000,
              0b000000000100010
    , 0b000000000101000, 0b000000000101010, 0b000000010000000, 0b000000010000010, 0b000000010001000, 0b000000010001010,
              0b000000010100000
    , 0b000000010100010, 0b000000010101000, 0b000000010101010, 0b000001000000000, 0b000001000000010, 0b000001000001000,
              0b000001000001010
    , 0b000001000100000, 0b000001000100010, 0b000001000101000, 0b000001000101010, 0b000001010000000, 0b000001010000010,
              0b000001010001000
    , 0b000001010001010, 0b000001010100000, 0b000001010100010, 0b000001010101000, 0b000001010101010, 0b000100000000000,
              0b000100000000010
    , 0b000100000001000, 0b000100000001010, 0b000100000100000, 0b000100000100010, 0b000100000101000, 0b000100000101010,
              0b000100010000000
    , 0b000100010000010, 0b000100010001000, 0b000100010001010, 0b000100010100000, 0b000100010100010, 0b000100010101000,
              0b000100010101010
    , 0b000101000000000, 0b000101000000010, 0b000101000001000, 0b000101000001010, 0b000101000100000, 0b000101000100010,
              0b000101000101000
    , 0b000101000101010, 0b000101010000000, 0b000101010000010, 0b000101010001000, 0b000101010001010, 0b000101010100000,
              0b000101010100010
    , 0b000101010101000, 0b000101010101010]

# for β state, we need to convert list_contain_15_bits_b_r into integer components
# for i in range(len(list_contain_15_bits_b_r)):
#     s = [str(integer) for integer in list_contain_15_bits_b_r[i]]
#     a_string = "".join(s)
#     res = int(a_string)
#     print(res)
bit_list_0 = [0b010101010101010, 0b010101010101000, 0b010101010100010, 0b010101010100000, 0b010101010001010,
              0b010101010001000
    , 0b010101010000010, 0b010101010000000, 0b010101000101010, 0b010101000101000, 0b010101000100010
    , 0b010101000100000, 0b010101000001010, 0b010101000001000, 0b010101000000010, 0b010101000000000, 0b010100010101010,
              0b010100010101000
    , 0b010100010100010, 0b010100010100000, 0b010100010001010, 0b010100010001000, 0b010100010000010, 0b010100010000000,
              0b010100000101010
    , 0b010100000101000, 0b010100000100010, 0b010100000100000, 0b010100000001010, 0b010100000001000, 0b010100000000010,
              0b010100000000000
    , 0b010001010101010, 0b010001010101000, 0b010001010100010, 0b010001010100000, 0b010001010001010, 0b010001010001000,
              0b010001010000010
    , 0b010001010000000, 0b010001000101010, 0b010001000101000, 0b010001000100010, 0b010001000100000, 0b010001000001010,
              0b010001000001000
    , 0b010001000000010, 0b010001000000000, 0b010000010101010, 0b010000010101000, 0b010000010100010, 0b010000010100000,
              0b010000010001010
    , 0b010000010001000, 0b010000010000010, 0b010000010000000, 0b010000000101010, 0b010000000101000, 0b010000000100010,
              0b010000000100000
    , 0b010000000001010, 0b010000000001000, 0b010000000000010, 0b010000000000000]

bit_list_1 = []
bit_list_2 = []
bit_list_3 = []
bit_list_4 = []


# 1/2 to be positive and 1/2 to be negative
# postive term
def new_bit_list(bit_list_before, bit_list_after, stabilizer_in_use):
    for i in bit_list_before:
        bit_list_after.append(i)
        bit_list_after.append(i ^ stabilizer_list[stabilizer_in_use])
    return bit_list_after


new_bit_list(bit_list_0, bit_list_1, 0)
new_bit_list(bit_list_1, bit_list_2, 1)
new_bit_list(bit_list_2, bit_list_3, 2)
new_bit_list(bit_list_3, bit_list_4, 3)


# coversion
def convert_binary_list(bit_list_input):
    binary_bit_list = []
    for i in bit_list_input:
        binary_bit_list.append(bin(i))
    return binary_bit_list


# print(convert_binary_list(bit_list_1))
# print(convert_binary_list(bit_list_2))
# print(convert_binary_list(bit_list_3))
# print(convert_binary_list(bit_list_4))

# negative term
recovery_bit_list_1 = [term for term in bit_list_1 if term not in bit_list_0]
recovery_bit_list_2 = [term for term in bit_list_2 if term not in bit_list_1]
recovery_bit_list_3 = [term for term in bit_list_3 if term not in bit_list_2]
recovery_bit_list_4 = [term for term in bit_list_4 if term not in bit_list_3]
# print(convert_binary_list(recovery_bit_list_1))
# print(convert_binary_list(recovery_bit_list_2))
# print(convert_binary_list(recovery_bit_list_3))
# print(convert_binary_list(recovery_bit_list_4))

# incidentally they are the same as bit_list_0
recovery_list = bit_list_r

# test recovery for bit_list_4
# create sub_list
sub_list_0 = bit_list_4[0:16]


# check recovery for sub_list
def check_recovery_list(sub_list, recovery_in_use):
    recovery_sub_list = []
    for i in sub_list:
        recovery_sub_list.append(i ^ recovery_list[recovery_in_use])
    return recovery_sub_list == sub_list_0


# for i in range(len(bit_list_0)):
#     print(check_recovery_list(bit_list_4[i*16:(i+1)*16],i))

# find correspond syndrome in Z stabilizer

# [1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
# [1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0]
# [0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0]
# [0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0]


z_stabilizer_list = [[1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                     [1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
                     [0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
                     [0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
                     # add one
                     [0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


# print(list_contain_15_bits_a[1][13])
# print(z_stabilizer_list[0][1])

def syn_stabilizer_list(id_15_bits_list, aim_list):
    sub_syn_list = []
    a_sum = 0
    for j in range(len(z_stabilizer_list)):
        for k in range(14):
            if aim_list[id_15_bits_list][k] == 1 and z_stabilizer_list[j][k] == 1:
                a_sum = a_sum + 1
                # print(a_sum)
        if a_sum % 2 == 1:
            sub_syn_list.append(j)
        a_sum = 0
    return sub_syn_list


# print(syn_stabilizer_list(7))
# print(syn_stabilizer_list(8))

syn_list_a = []
syn_list_b = []

for i in range(len(list_contain_15_bits_a)):
    syn_list_a.append(syn_stabilizer_list(i, list_contain_15_bits_a))
    syn_list_b.append(syn_stabilizer_list(i, list_contain_15_bits_b_r))

print(syn_list_a)
print(syn_list_b)

# check repeat element
# Convert to set
duplist = []  # empty list to hold the duplicate elements from the list
newlist = []

for i in syn_list_a:
    if i not in newlist:
        newlist.append(i)
    else:
        duplist.append(i)

print(len(newlist))
print(len(duplist))

# test Z stabilizer
test_z_stabilizer = [0b110011000000000,0b011010010000000,0b110000001100000,0b011000001001000,0b010010001000010,0b011110000000000]
state_list = bit_list_r[0:16]
# state_list = bit_list_0[0:16]

for i in range(len(state_list)):
    for j in range(len(test_z_stabilizer)):
        if (test_z_stabilizer[j] + state_list[i])%2 == 1:
            print("stabizer is bad")
