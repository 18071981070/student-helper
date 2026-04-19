import re

class SecurityFilter:
    def __init__(self):
        self.sensitive_words = [
            '毒品', '赌博', '色情', '暴力', '反动', '颠覆', '分裂',
            '武器', '爆炸物', '制造炸弹', '毒品配方', '赌博网站',
            '色情网站', '暴力内容', '反动言论', '分裂国家',
            '身份证', '银行卡', '密码', '手机号', '住址'
        ]
        
        self.malicious_patterns = [
            r'system\(.*\)',
            r'exec\(.*\)',
            r'eval\(.*\)',
            r'os\.[a-zA-Z_]+\(.*\)',
            r'subprocess\.[a-zA-Z_]+\(.*\)',
            r'open\(.*\)',
            r'file\(.*\)',
            r'__import__\(.*\)',
            r'compile\(.*\)',
        ]
    
    def contains_sensitive_content(self, text):
        for word in self.sensitive_words:
            if word in text:
                return True
        
        for pattern in self.malicious_patterns:
            if re.search(pattern, text, re.IGNORECASE):
                return True
        
        return False

security_filter = SecurityFilter()