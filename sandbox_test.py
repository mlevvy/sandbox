from sut.salesforce import Salesforce


def test_mocker(mocker):
    print("Running test mocker")
    function = mocker.patch("sut.connector.Connector.do_next")
    function.side_effect = lambda *args, **kwargs: "MOCK"
    d1 = Salesforce()
    assert d1.do_next() == "MOCK"


def test_2(module_scope, session_scope, class_scope, function_scope):
    print("Running test 2")
    assert module_scope._get_name() == "Module"
    assert session_scope._get_name() == "Session"
    assert class_scope._get_name() == "Class"
    assert function_scope._get_name() == "Function"


def test_3(module_scope, session_scope, class_scope, function_scope):
    print("Running test 3")
    assert module_scope._get_name() == "Module"
    assert session_scope._get_name() == "Session"
    assert class_scope._get_name() == "Class"
    assert function_scope._get_name() == "Function"


def test_4(module_scope, session_scope, class_scope, function_scope):
    print("Running test 4")
    assert module_scope._get_name() == "Module"
    assert session_scope._get_name() == "Session"
    assert class_scope._get_name() == "Class"
    assert function_scope._get_name() == "Function"


class TestClass():
    def test_class_1(self, module_scope, session_scope, class_scope, function_scope):
        print("Running test class 1")
        assert module_scope._get_name() == "Module"
        assert session_scope._get_name() == "Session"
        assert class_scope._get_name() == "Class"
        assert function_scope._get_name() == "Function"

    def test_class_2(self, module_scope, session_scope, class_scope, function_scope):
        print("Running test class 2")
        assert module_scope._get_name() == "Module"
        assert session_scope._get_name() == "Session"
        assert class_scope._get_name() == "Class"
        assert function_scope._get_name() == "Function"

