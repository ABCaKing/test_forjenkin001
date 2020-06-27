import pytest, allure

class Test_allure():

    def setup(self):
        pass
    def teardown(self):
        pass

    @allure.issue
    @pytest.mark.paramtrize("a", [1,2,3])
    @allure.step("Œ“ «≤‚ ‘≤Ω÷Ë001")
    def test_al(self, a):
        assert a !=2