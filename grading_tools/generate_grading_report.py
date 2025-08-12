from typing import Dict, Any
from smolagents import tool # Importe o decorador @tool da sua biblioteca

@tool
def generate_grading_report(
    qr_code_info: Dict[str, Any], 
    student_answers: Dict[str, Any]
) -> str:
    """
    Generates a formatted grading report by comparing student answers to the official answer key.

    Args:
        qr_code_info (Dict[str, Any]): A dictionary containing the test's official information,
                                       including 'assessment_id', 'quantity_of_questions', and
                                       a 'correct_alternatives' dictionary.
        student_answers (Dict[str, Any]): A dictionary containing the student's marked answers,
                                          with question numbers as keys.

    Returns:
        str: A formatted markdown string containing the full test scoring report.
    """
    # 1. Extração segura dos dados de entrada
    assessment_id = qr_code_info.get('assessment_id', 'N/A')
    correct_alternatives = qr_code_info.get('correct_alternatives', {})
    
    # Usa o total de questões do gabarito como fonte da verdade, mas exibe o número do QR code.
    total_questions_in_key = len(correct_alternatives)
    total_questions_display = qr_code_info.get('quantity_of_questions', total_questions_in_key)

    # 2. Inicialização dos contadores e resultados
    correct_count = 0
    incorrect_count = 0
    blank_count = 0
    results = {}

    # 3. Comparação das respostas (iterando sobre as chaves do gabarito)
    # Ordena as chaves numericamente para garantir que o relatório seja gerado na ordem correta.
    question_keys_sorted = sorted(correct_alternatives.keys(), key=int)

    for question_key in question_keys_sorted:
        correct_answer = correct_alternatives.get(question_key, [])
        student_answer = student_answers.get(question_key, [])

        # A lógica de comparação é a mesma que você forneceu, pois é ótima.
        # O uso de sorted() lida com questões de múltipla marcação.
        if not student_answer:
            results[question_key] = "⚪"  # Em branco
            blank_count += 1
        elif sorted(correct_answer) == sorted(student_answer):
            results[question_key] = "✅"  # Correta
            correct_count += 1
        else:
            results[question_key] = "❌"  # Incorreta
            incorrect_count += 1
    
    # 4. Preparação do relatório final em formato de string
    report_header = f"""---
### **Test Scoring Report**
- **Assessment ID:** {assessment_id}
- **Total Questions:** {total_questions_display}

#### **Performance Summary**
- **✅ Correct:** {correct_count}
- **❌ Incorrect:** {incorrect_count}
- **⚪ Blank:** {blank_count}
- **🔢 Final Score:** {correct_count}

#### **Question-by-Question Breakdown**"""

    report_body_list = []
    for question_key in question_keys_sorted:
        status = results.get(question_key, "❓") # Usa ❓ se a questão não foi processada
        report_body_list.append(f"- **Question {question_key}:** {status}")
    
    report_body = "\n".join(report_body_list)

    # 5. Retorna o relatório completo
    return f"{report_header}\n{report_body}\n---"

