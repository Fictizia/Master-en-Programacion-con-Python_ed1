from collections import defaultdict


class Parser:

    _valid_tokens = list('+-><[].')

    def parse(self, source):
        def is_valid(token):
            return token in self._valid_tokens

        return list(filter(is_valid, source))


class EventEmitter:

    def __init__(self):
        self._listeners = defaultdict(lambda: [])

    def on(self, event, listener):
        self._listeners[event].append(listener)

    def emit(self, event, *args, **kwargs):
        for listener in self._listeners[event]:
            listener(*args, **kwargs)


class Compiler(EventEmitter):

    _translations_map = {
        '+': 'AddOne',
        '-': 'SubOne',
        '>': 'Next',
        '<': 'Previous',
        '[': 'StartLoop',
        ']': 'EndLoop',
        '.': 'Output'
    }

    def compile(self, source):
        self._notify_start()
        instructions = Parser().parse(source)
        total = len(instructions)
        translation = []
        for index, line in enumerate(instructions):
            self._notify_progress(index/total)
            translation.append(self._translations_map[line])

        self._notify_end()
        return '\n'.join(translation)

    def _notify_start(self):
        self.emit('compilation-started')

    def _notify_end(self):
        self.emit('compilation-finished')

    def _notify_progress(self, progress):
        self.emit('compilation-progress', progress)


class ProgressDisplay:

    def connect(self, compiler):
        def _print_start():
            print('Compilation started')

        def _print_end():
            print('Compilation end')

        def _print_progress(progress):
            print(f'{progress:.2%}')

        compiler.on('compilation-started', _print_start)
        compiler.on('compilation-finished', _print_end)
        compiler.on('compilation-progress', _print_progress)


if __name__ == '__main__':
    program = '+++>++[-<+>].'
    compiler = Compiler()
    progress = ProgressDisplay()
    progress.connect(compiler)
    print(compiler.compile(program))
