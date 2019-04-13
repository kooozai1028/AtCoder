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
