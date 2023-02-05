import gspread


class Logs:
    def __init__(self, sh_name, wks_name):
        print('Logs Class created')
        sa = gspread.service_account()
        self.sh = sa.open(sh_name)
        self.wks = self.sh.worksheet(wks_name)
        self.buff = self.wks.get(f'A1:H{self.init_amount() + 1}')

    def init_amount(self):
        ow = 1
        for i in range(self.wks.row_count - 1):
            if self.wks.acell(f'A{i + 1}').value == None:
                return i - 1
    def amount(self):
        return len(self.buff)-1

    def get_header(self):
        buff = self.buff
        header = []
        for elem in buff[0]:
            header.append(elem)
        return header

    def by_num(self, num):
        return self.buff[num]

    def as_dict(self):
        logs = {}
        buff = self.buff
        #print(buff)
        header = self.get_header()
        #print(f'buff:{buff}\nheader:{header}')
        for col in range(len(header)):
            #print(f'Current column: {header[col]}')
            for row in range(self.amount()):
                #print(f'Current row: {row}')
                if row == 0:
                    logs[header[col]]=[buff[row+1][col]]
                else:
                    try:
                        logs[header[col]].append(buff[row+1][col])
                    except:
                        logs[header[col]].append(None)
        return logs

    def __str__(self):
        log_dict = self.as_dict()
        output = ''
        for key in log_dict.keys():
            output+=f'\n{key}\n'
            for value in log_dict[key]:
                output+=f'-> {value}\n'
        return output





