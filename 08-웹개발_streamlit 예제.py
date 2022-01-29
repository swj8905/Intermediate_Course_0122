import streamlit as st

st.text("Hello World")

st.write("이런 것도 됩니다.")
st.write("# 이런 것도 됩니다.")
st.write("## 이런 것도 됩니다.")
st.write("### 이런 것도 됩니다.")
st.write("#### 이런 것도 됩니다.")
st.write("##### 이런 것도 됩니다.")
st.write("###### 이런 것도 됩니다.")

st.write("**이런** 것도 됩니다.")
st.write("*이런* 것도 됩니다.")

st.write("----------------------")

st.write([0,1,2,3])
st.write({"짜장면":5000, "짬뽕":6000})
st.write("1 + 1 = ", 2)

st.write("https://www.naver.com")

st.code("""
foo = 10
if foo >= 0:
    print("OK")
else:
    print("NO")
""")

"이런 것도 됩니다."
"# 이런 것도 됩니다."

"""
# 매직 커맨드

https://www.naver.com

|       |   점수   |    평가     |
|-------|----------|-------------|
| 철수  |  90      | 참잘했습니다.|
| 영희  | 30       | 분발해주세요.|

```python
print("Hello World")
```
"""