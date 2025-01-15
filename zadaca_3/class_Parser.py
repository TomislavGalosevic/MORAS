class Parser:
    from parseLines import _parse_lines, _parse_line
    from parseSymbs import _init_symbols, _parse_symbols, _parse_labels, _parse_variables
    from parseComms import _init_comms, _parse_command, _parse_commands
    from parseMacros import _parse_macros, _parse_macro, _mv, _swp, _add, _while
    
    def __init__(self, filename):
        try:
            self._file = open(filename + ".asm", "r")
        except:
            Parser._error("File", -1, "Cannot read source file.")
            return

        self._lines = []
        
        try:
            self._read_lines()
        except:
            Parser._error("File", -1, "Cannot read source file.")
            return

        self._flag = True 
        self._line = -1   
        self._errm = ""  
        
        self._labels = {}
        self._variables = {}

        self._nest = 0

        self._parse_lines()
        if self._flag == False:
            Parser._error("pri parsiranju", self._line, self._errm)
            return

        self._parse_macros()
        if self._flag == False:
            Parser._error("$", self._line, self._errm)
            return

        self._parse_symbols()
        if self._flag == False:
            Parser._error("SYM", self._line, self._errm)
            return
            
        self._parse_commands()
        if self._flag == False:
            Parser._error("COM", self._line, self._errm)
            return
        
        try:
            self._outfile = open(filename + ".hack", "w")
        except:
            Parser._error("File", -1, "Cannot open output file")
            return

        try:
            self._write_file()
        except:
            Parser._error("File", -1, "Cannot write to output file")
            return          

    def _read_lines(self):
        n = 0
        for line in self._file:
            self._lines.append((line, n, n));
            n += 1

    def _write_file(self):
        for (line, p, o) in self._lines:
            self._outfile.write(line)
            if (line[-1] != "\n"):
                self._outfile.write("\n")

    def _iter_lines(self, func):
        i = 0
        newlines = []
        for (line, p, o) in self._lines:
            func1 = func(line, p, o)
            if isinstance(func1, list):
                for l in func1:
                    if len(l) > 0:
                        newlines.append((l, i, o))
                        if l[0] != "(":
                            i += 1
            else:
                newline = func1
                if len(newline) > 0:
                    newlines.append((newline, i, o))
                    if newline[0] != "(":
                        i += 1
        self._lines = newlines
    @staticmethod
    def _error(src, line, msg):
        if len(src) > 0 and line > -1:
            print("[" + src + ", " + str(line) + "] " + msg)
        elif len(src) > 0:
            print("[" + src + "] " + msg)
        else:
            print(msg)  

if __name__ == "__main__":
    Parser("tt")