def test_5(module_scope, session_scope, class_scope, function_scope):
    print("Running test 5")
    assert module_scope._get_name() == "Module"
    assert session_scope._get_name() == "Session"
    assert class_scope._get_name() == "Class"
    assert function_scope._get_name() == "Function"
