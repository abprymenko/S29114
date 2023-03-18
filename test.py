import studentinfo as st
st.Student.amount_students += 3
print(f"Total amount of students: {st.Student.amount_students}")
andrii = st.Student("Andrii", 15, 170)
print(andrii.GetFullInfo())
#print((andrii.amount_students))
dima = st.Student("Dima", 14, 180)
print(dima.GetFullInfo())
#print((dima.amount_students))
roma = st.Student("Roma", 15, 183)
print(roma.GetFullInfo())