import pandas as pd
from solution import add_virtual_column


def test_sum_of_two_columns():
    df = pd.DataFrame([[1, 1]] * 2, columns = ["label_one", "label_two"])
    df_expected = pd.DataFrame([[1, 1, 2]] * 2, columns = ["label_one", "label_two", "label_three"])
    df_result = add_virtual_column(df, "label_one+label_two", "label_three")
    assert df_result.equals(df_expected), f"1) The function should sum the columns: label_one and label_two.\n\nResult:\n\n{df_result}\n\nExpected:\n\n{df_expected}"
    print("\n1) Test 'test_sum_of_two_columns' ✅")


def test_multiplication_of_two_columns():
    df = pd.DataFrame([[1, 1]] * 2, columns = ["label_one", "label_two"])
    df_expected = pd.DataFrame([[1, 1, 1]] * 2, columns = ["label_one", "label_two", "label_three"])
    df_result = add_virtual_column(df, "label_one * label_two", "label_three")
    assert df_result.equals(df_expected), f"2) The function should multiply the columns: label_one and label_two.\n\nResult:\n\n{df_result}\n\nExpected:\n\n{df_expected}"
    print("\n2) Test 'test_multiplication_of_two_columns' ✅")


def test_subtraction_of_two_columns():
    df = pd.DataFrame([[1, 1]] * 2, columns = ["label_one", "label_two"])
    df_expected = pd.DataFrame([[1, 1, 0]] * 2, columns = ["label_one", "label_two", "label_three"])
    df_result = add_virtual_column(df, "label_one - label_two", "label_three")
    assert df_result.equals(df_expected), f"3) The function should subtract the columns: label_one and label_two.\n\nResult:\n\n{df_result}\n\nExpected:\n\n{df_expected}"
    print("\n3) Test 'test_subtraction_of_two_columns' ✅")


def test_empty_result_when_invalid_labels():
    df = pd.DataFrame([[1, 2]] * 3, columns = ["label_one", "label_two"])
    df_result = add_virtual_column(df, "label_one + label_two", "label3")
    assert df_result.empty, f"4) Should return an empty df when the \"new_column\" is invalid.\n\nResult:\n\n{df_result}\n\nExpected:\n\nEmpty df"
    print("\n4) Test 'test_empty_result_when_invalid_labels' ✅")


def test_empty_result_when_invalid_labels_from_pdf():
    df = pd.DataFrame([[1, 2]] * 3, columns = ["label_one", "label_two"])
    df_result = add_virtual_column(df, "label_one + label_two", "label3")
    assert df_result.empty, f"5) Should return an empty df when the \"new_column\" is invalid.\n\nResult:\n\n{df_result}\n\nExpected:\n\nEmpty df"
    df = pd.DataFrame([[1, 2]] * 3, columns = ["label-one", "label_two"])
    df_result = add_virtual_column(df, "label-one + label_two", "label")
    assert df_result.empty, f"5) Should return an empty df when both df columns and roles are invalid.\n\nResult:\n\n{df_result}\n\nExpected:\n\nEmpty df"
    df = pd.DataFrame([[1, 2]] * 3, columns = ["label-one", "label_two"])
    df_result = add_virtual_column(df, "label_one + label_two", "label")
    assert df_result.empty, f"5) Should return an empty df when a df column is invalid.\n\nResult:\n\n{df_result}\n\nExpected:\n\nEmpty df"
    print("\n5) Test 'test_empty_result_when_invalid_labels_from_pdf' ✅")


def test_empty_result_when_invalid_rules():
    df = pd.DataFrame([[1, 1]] * 2, columns = ["label_one", "label_two"])
    df_result = add_virtual_column(df, "label&one + label_two", "label_three")
    assert df_result.empty, f"6) Should return an empty df when the role have invalid character: '&'.\n\nResult:\n\n{df_result}\n\nExpected:\n\nEmpty df"
    df_result = add_virtual_column(df, "label_five + label_two", "label_three")
    assert df_result.empty, f"6) Should return an empty df when the role have a column which isn't in the df: 'label_five'.\n\nResult:\n\n{df_result}\n\nExpected:\n\nEmpty df"
    print("\n6) Test 'test_empty_result_when_invalid_rules' ✅")

def test_empty_result_when_invalid_rules_from_pdf():
    df = pd.DataFrame([[1, 1]] * 2, columns = ["label_one", "label_two"])
    df_result = add_virtual_column(df, "label_one \\ label_two", "label_three")
    assert df_result.empty, f"7) Should return an empty df when the role have invalid character: '\\'.\n\nResult:\n\n{df_result}\n\nExpected:\n\nEmpty df"
    df_result = add_virtual_column(df, "label&one + label_two", "label_three")
    assert df_result.empty, f"7) Should return an empty df when the role have invalid character: '&'.\n\nResult:\n\n{df_result}\n\nExpected:\n\nEmpty df"
    df_result = add_virtual_column(df, "label_five + label_two", "label_three")
    assert df_result.empty, f"7) Should return an empty df when the role have a column which isn't in the df: 'label_five'.\n\nResult:\n\n{df_result}\n\nExpected:\n\nEmpty df"
    print("\n7) Test 'test_empty_result_when_invalid_rules_from_pdf' ✅")

def test_when_extra_spaces_in_rules():
    df = pd.DataFrame([[1, 1]] * 2, columns = ["label_one", "label_two"])
    df_expected = pd.DataFrame([[1, 1, 2]] * 2, columns = ["label_one", "label_two", "label_three"])
    df_result = add_virtual_column(df, "label_one + label_two ", "label_three")
    assert df_result.equals(df_expected), f"8) Should work when the role have spaces between the operation and the column.\n\nResult:\n\n{df_result}\n\nExpected:\n\n{df_expected}"
    df_result = add_virtual_column(df, "  label_one + label_two ", "label_three")
    assert df_result.equals(df_expected), f"8) Should work when the role have extra spaces in the start/end.\n\nResult:\n\n{df_result}\n\nExpected:\n\n{df_expected}"
    print("\n8) Test 'test_when_extra_spaces_in_rules' ✅")

def test_when_extra_spaces_in_rules_from_pdf():
    df = pd.DataFrame([[1, 1]] * 2, columns = ["label_one", "label_two"])
    df_expected = pd.DataFrame([[1, 1, 2]] * 2, columns = ["label_one", "label_two", "label_three"])
    df_result = add_virtual_column(df, "label_one+label_two", "label_three")
    assert df_result.equals(df_expected), f"9) Should work when the role haven't spaces between the operation and the column.\n\nResult:\n\n{df_result}\n\nExpected:\n\n{df_expected}"
    df_result = add_virtual_column(df, "label_one + label_two ", "label_three")
    assert df_result.equals(df_expected), f"9) Should work when the role have spaces between the operation and the column.\n\nResult:\n\n{df_result}\n\nExpected:\n\n{df_expected}"
    df_result = add_virtual_column(df, " label_one + label_two ", "label_three")
    assert df_result.equals(df_expected), f"9) Should work when the role have extra spaces in the start/end.\n\nResult:\n\n{df_result}\n\nExpected:\n\n{df_expected}"
    print("\n9) Test 'test_when_extra_spaces_in_rules_from_pdf' ✅")

#Below are unit tests that I added to check some additional edge-cases

def test_edge_case_forbidden_operator():
    #Checks if the operators other than +, -, * are acceptes
    df = pd.DataFrame({'a': [10], 'b': [2]})
    result = add_virtual_column(df, "a / b", "res")
    assert result.empty, "10) Should return empty df, because '/' is not allowed."
    print("\n10) Test 'test_edge_case_forbidden_operator' ✅")

def test_edge_case_missing_column_in_df():
    #Checks the behavior of the function when role refers to non-existent column
    df = pd.DataFrame({'a': [1, 2], 'b': [3, 4]})
    result = add_virtual_column(df, "a + c", "res")
    assert result.empty, "11) Should return empty df, because column 'c' doesn't exist."
    print("\n11) Test 'test_edge_case_missing_column_in_df' ✅")


def test_edge_case_keyword_inf():
    #Checks the behavior of the eval() when column uses keyword referring to infinity
    df = pd.DataFrame({'qty': [10, 20]})
    result = add_virtual_column(df, "qty * inf", "total")
    assert result.empty, "12) Should return empty df, because 'inf' is a keyword and not a column."
    print("\n12) Test 'test_edge_case_keyword_inf' ✅")


def test_edge_case_keyword_null_column():
    df = pd.DataFrame({'null': [10, 20], 'price': [5, 5]})
    result = add_virtual_column(df, "null * price", "total")
    actual_val = result["total"].iloc[0] if not result.empty else None
    assert result.empty, "13) Should return empty df, because 'null' cannot be the name of the column."
    print("\n13) Test '13) test_edge_case_keyword_null_column' ✅")

test_sum_of_two_columns()
test_multiplication_of_two_columns()
test_subtraction_of_two_columns()
test_empty_result_when_invalid_labels()
test_empty_result_when_invalid_labels_from_pdf()
test_empty_result_when_invalid_rules()
test_empty_result_when_invalid_rules_from_pdf()
test_when_extra_spaces_in_rules()
test_when_extra_spaces_in_rules_from_pdf()
test_edge_case_forbidden_operator()
test_edge_case_missing_column_in_df()
test_edge_case_keyword_inf()
test_edge_case_keyword_null_column()