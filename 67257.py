import re
from itertools import permutations


def get_opPermu(expr):
    # expr에 쓰인 연산자(*,+,-) 추출
    # "50*6-3*20" => ["*","-"]
    op = list(set(list(("".join(re.split("[\d]", expr)).split())[0])))
    op_permu = list(permutations(op))  # 연산자 순열 생성

    return op_permu


def split_expr(expr):
    # "50*6-3*20" -> [50, '*', 6, '-', 3, '*', 20]
    start = 0
    dummy = []
    for idx in range(len(expr)):
        if expr[idx] in ("*", "-", "+"):
            dummy.append(int(expr[start:idx]))
            dummy.append(expr[idx])
            start = idx+1
    dummy.append(int(expr[start:]))

    return dummy


def cal_postfix(post_expr):
    num_stack = []
    for elem in post_expr:
        if elem in ("*", "-", "+"):
            val1 = num_stack.pop(-1)
            val2 = num_stack.pop(-1)

            if elem == "*":
                elem_sum = val2 * val1
            elif elem == "-":
                elem_sum = val2 - val1
            elif elem == "+":
                elem_sum = val2 + val1

            num_stack.append(elem_sum)
        else:
            num_stack.append(elem)
    return num_stack.pop(0)


def get_maxPostfixValue(spl_expr, op_permu):
    vals = []
    op_stack = []
    post_expr = []
    for op_part in op_permu:
        for item in spl_expr:
            if item in ("*", "-", "+"):
                if not op_stack:
                    op_stack.append(item)
                else:  # 연산자 우선순위 비교
                    while True:
                        if op_part.index(item) >= op_part.index(op_stack[-1]):
                            post_expr.append(op_stack.pop(-1))
                            op_stack.append(item)
                        else:
                            op_stack.append(item)
                            break
            else:
                post_expr.append(item)
        while op_stack:
            post_expr.append(op_stack.pop(-1))

        val = cal_postfix(post_expr)
        vals.append(val)

        op_stack.clear()
        post_expr.clear()
    return max(vals)


def solution(expression):
    op_permu = get_opPermu(expression)
    spl_expr = split_expr(expression)
    answer = get_maxPostfixValue(spl_expr, op_permu)

    return answer


solution("100-200*300-500+20")
