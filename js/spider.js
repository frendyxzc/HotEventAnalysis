/*global phantom*/
"use strict";

// ������Դ�ȴ�ʱ�䣬������Դ���غ���Ҫ����������Դ
var resourceWait = 500;
var resourceWaitTimer;
// ���ȴ�ʱ��
var maxWait = 5000;
var maxWaitTimer;
// ��Դ����
var resourceCount = 0;

// PhantomJS WebPageģ��
var page = require('webpage').create();
// NodeJS ϵͳģ��
var system = require('system');
// ��CLI�л�ȡ�ڶ�������ΪĿ��URL
var url = system.args[1];

// ����PhantomJS�Ӵ���С
page.viewportSize = {
    width: 1280,
    height: 1014
};

// ��ȡ����
var capture = function(errCode){
    // �ⲿͨ��stdout��ȡҳ������
    console.log(page.content);
    // �����ʱ��
    clearTimeout(maxWaitTimer);
    // ������ɣ������˳�
    phantom.exit(errCode);

};

// ��Դ���󲢼���
page.onResourceRequested = function(req){
    resourceCount++;
    clearTimeout(resourceWaitTimer);
};

// ��Դ�������
page.onResourceReceived = function (res) {
    // chunkģʽ��HTTP�ذ������δ���resourceReceived�¼�����Ҫ�ж���Դ�Ƿ��Ѿ�end
    if (res.stage !== 'end'){
        return;
    }

    resourceCount--;

    if (resourceCount === 0){
        // ��ҳ����ȫ����Դ��������Ϻ󣬽�ȡ��ǰ��Ⱦ������html
        // ����onResourceReceived����Դ������Ͼ������������ˣ�������Ҫ��һЩʱ����JS�ܽ�������
        // ����Ĭ��Ԥ��500����
        resourceWaitTimer = setTimeout(capture, resourceWait);
    }
};

// ��Դ���س�ʱ
page.onResourceTimeout = function(req){
    resouceCount--;
};

// ��Դ����ʧ��
page.onResourceError = function(err){
    resourceCount--;
};

// ����userAgent���ƹ�Sina Visitor System
page.settings.userAgent = 'spider';
// ��ҳ��
page.open(url, function (status) {
    if (status !== 'success') {
        phantom.exit(1);
    } else {
        // ����ҳ��ĳ�ʼhtml���سɹ��󣬿�����ʱ��
        // ���������ʱ�䣨Ĭ��5�룩��ʱ�򣬽�ȡ��һʱ����Ⱦ������html
        maxWaitTimer = setTimeout(function(){
            capture(2);
        }, maxWait);
    }
});