import random
from tkinter import *

# 답변 리스트
answer = [
    "실패해선 안된다는 생각에 집착하지 말라.", "온전히 당신에게 달려있다.",
    "당신의 생각대로이다.", "눈 앞의 정답을 놓치고 있다", "그렇다.",
    "그럴 수는 없다.", "당신의 삶에 크게\n영향을 주지 않을 것이다.",
    "후회없이 행하라.", "가장 가까운 사람의 의견을 믿어라.", "그럴 만 하다.",
    "결과보다 당신이 하고 있는\n일 자체가 중요하다.", "크게 신경쓰지 말라.",
    "도움을 받으라.", "온전히 당신에게 달려있다.", "슬슬 이루어져가고 있다.",
    "안심하라.", "실망할 일은 없어보인다.", "함께 할 사람을 찾아보라",
    "잘못될 수 있다.", "그럴 만 하다.", "아주 중요한 기회가 찾아온다.",
    "혼란에 빠지게 된다.", "충분히 즐길 수 있다.", "두번째 길이 나타날 것이다."
]

# 버튼 클릭 시 호출되는 함수
def click_btn():
    random_answer = random.randint(0, len(answer) - 1)
    canvas.itemconfig(an, text=answer[random_answer])

# 윈도우 생성
window = Tk()
window.title("고민ZERO")

# 캔버스 생성
canvas = Canvas(window, width=500, height=500)
canvas.pack()

# 이미지 로드
img = PhotoImage(file="img.png")
canvas.create_image(250, 250, image=img)

# 텍스트 생성
an = canvas.create_text(
    250, 220, text="고민ZERO\n'당신의 고민을 해결해드리겠습니다.'",
    fill="white", font=("나눔바른펜", 20, "bold")
)

# 버튼 생성
btn = Button(
    window, text="클릭", font=("나눔바른펜", 20, "bold"),
    bg="white", command=click_btn
)
btn.place(x=210, y=400)

# 메인 루프 실행
window.mainloop()