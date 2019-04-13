#一番シンプル
# a = input()
# print(min(a.count('1'), a.count('0')) * 2)

#俺の思考回路に近いやつ
S = input()
st = []
ans = 0
for c in S:
    if st and st[0] != c:
        st.pop()
        ans += 2
    else:
        st.append(c)
print(ans)
print(st)

# list = list(input())
#
# temp = list[0]
# ans = []
#
# for i in range(1,len(list)-2):
#     if list[i] != temp:
#         temp = list[i]
#         if list[i] != list[i+1]:
#             ans.append(list[i])
#
# print(ans)