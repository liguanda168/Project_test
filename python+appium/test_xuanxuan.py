import pytest
from appium import webdriver


class Test():
#��
    def setup_class(self):
        #��ʼ��driver
        cap = {
            "platformName": "Android",
            "deviceName": "127.0.0.1:62001",
            "appPackage": "com.cnezsoft.xxm",
            "appActivity": ".MainActivity",
            "noReset": True
        }
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", cap)
        self.driver.implicitly_wait(20)

#�ر�
    def teardown(self):
        #�ر�driver
        self.driver.quit()

# 1.�ղ�������wasd
    def test_Shoucangaaa(self):
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.view.View[2]").click()
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]").click()
        self.driver.find_element_by_xpath("//*[@text='��ʾ�˵�']").click()
        self.driver.find_element_by_xpath("//*[@text='�ղ�']").click()

# 2.ȡ���ղ�������wasd
    def test_Cancelshoucangaaa(self):
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.view.View[2]").click()
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]").click()
        self.driver.find_element_by_xpath("//*[@text='��ʾ�˵�']").click()
        self.driver.find_element_by_xpath("//*[@text='ȡ���ղ�']").click()

#3.��ʾwasd��Ա�б�
    def test_ShowMembers(self):
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.view.View[2]").click()
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]").click()
        self.driver.find_element_by_xpath("//*[@text='��ʾ�˵�']").click()
        self.driver.find_element_by_xpath("//*[@text='��Ա�б�']").click()

#4.ȡ��������������wasd
    def test_CancelRename(self):
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.view.View[2]").click()
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]").click()
        self.driver.find_element_by_xpath("//*[@text='��ʾ�˵�']").click()
        self.driver.find_element_by_xpath("//*[@text='������']").click()
        self.driver.find_element_by_xpath("//*[@text='ȡ��']").click()

#5.ͬ��������wasd�������Ϣ
    def test_Refresh(self):
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.view.View[2]").click()
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]").click()
        self.driver.find_element_by_xpath("//*[@text='��ʾ�˵�']").click()
        self.driver.find_element_by_xpath("//*[@text='ͬ���������Ϣ']").click()

#6.��������wasd�����ղ�����
    def test_TakepictureAndcend(self):
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.view.View[2]").click()
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]").click()
        self.driver.find_element_by_xpath("//*[@text='������������']").click()
        self.driver.find_element_by_xpath("//*[@text='����']").click()
        self.driver.find_element_by_id("com.android.camera2:id/shutter_button").click()
        self.driver.find_element_by_id("com.android.camera2:id/done_button").click()


#7.��������wasd��ѡ����lgd����
    def test_ChatWithlizhe1(self):
        self.driver.find_element_by_xpath("//*[@text='��������']").click()
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.view.View/android.view.View[1]").click()
        self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.Button[2]").click()

#8.�鿴�ҵ�-���ڲ��ر�
    def test_MyAbout(self):
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.view.View[4]").click()
        self.driver.find_element_by_xpath("//*[@text='��ʾ�˵�']").click()
        self.driver.find_element_by_xpath("//*[@text='����']").click()
        self.driver.find_element_by_xpath("//*[@text='�ر�']").click()

#9.�鿴��˽����
    def test_MyAboutprivacypolicy(self):
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.view.View[4]").click()
        self.driver.find_element_by_xpath("//*[@text='��ʾ�˵�']").click()
        self.driver.find_element_by_xpath("//*[@text='����']").click()
        self.driver.find_element_by_xpath("//*[@text='��˽����']").click()

#10.������������
    def test_MyAboutweb(self):
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.view.View[4]").click()
        self.driver.find_element_by_xpath("//*[@text='��ʾ�˵�']").click()
        self.driver.find_element_by_xpath("//*[@text='����']").click()
        self.driver.find_element_by_xpath("//*[@text='http://xuan.im']").click()

#11.�鿴��¼�û���Ϣ
    def test_Mymessage(self):
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.view.View[4]").click()
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]/android.view.View").click()



#12.�˳�������
    def test_Exittaolunzu(self):
        self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.view.View[2]").click()
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]").click()
        self.driver.find_element_by_xpath("//*[@text='��ʾ�˵�']").click()
        self.driver.find_element_by_xpath("//*[@text='�˳�������']").click()
        self.driver.find_element_by_xpath("//*[@text='ȷ��']").click()

#13.�鿴lgd����
    def test_LookMaterial(self):
        self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.view.View[1]").click()
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]").click()
        self.driver.find_element_by_xpath("//*[@text='��ʾ�˵�']").click()
        self.driver.find_element_by_xpath("//*[@text='����']").click()

#14.ע��
    def test_MyCancel(self):
        self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.view.View[4]").click()
        self.driver.find_element_by_xpath("//*[@text='ע��']").click()
        self.driver.find_element_by_xpath("//*[@text='ȷ��']").click()



