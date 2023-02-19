# 03. Student Credits - Python Advanced Retake Exam - 14 December 2022
# https://judge.softuni.org/Contests/Practice/Index/3744#2
def students_credits(*args):
  dictionary = {}
  total_credits = 0
  for course_info in args:
    info_splitted = course_info.split("-")
    course_name = info_splitted[0]
    course_credit = int(info_splitted[1])
    max_points = int(info_splitted[2])
    dyan_points = int(info_splitted[3])
    dyan_credits = (dyan_points / max_points) * course_credit
    total_credits += dyan_credits
    dictionary[course_name] = dyan_credits
  
  dictionary_as_list = []
  
  if total_credits >= 240:
    dictionary_as_list.append(f"Diyan gets a diploma with {total_credits:.1f} credits.")
  else:
    difference = 240 - total_credits
    dictionary_as_list.append(f"Diyan needs {difference:.1f} credits more for a diploma.")


  dictionary_sorted = sorted(dictionary.items(), key= lambda x: -x[1])

  

  for key, value in dictionary_sorted:
    dictionary_as_list.append(f"{key} - {value:.1f}")
    
  return "\n".join(dictionary_as_list)  


print(
    students_credits(
        "Computer Science-12-300-250",
        "Basic Algebra-15-400-200",
        "Algorithms-25-500-490"
    )
)