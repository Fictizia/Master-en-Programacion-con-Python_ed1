from collections import defaultdict


class Parser:

    _valid_tokens = list('+-><[].')

    def parse(self, source):
        def is_valid(token):
            return token in self._valid_tokens

        return list(filter(is_valid, source))


class FakeParser(Parser):

    def parse(self, _):
        return list('+-<>[].')


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

    def __init__(self, parser):
        super().__init__()
        self._parser = parser

    def compile(self, source):
        self._notify_start()
        instructions = self._parser.parse(source)
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


class ProgressMeter:

    def connect(self, compiler):
        compiler.on('compilation-started', self._print_start)
        compiler.on('compilation-finished', self._print_end)
        compiler.on('compilation-progress', self._print_progress)

    def _print_start(self):
        print('Compilation started')

    def _print_end(self):
        print('Compilation end')

    def _print_progress(self, progress):
        print(f'{progress:.2%}')


class ProgressBar(ProgressMeter):

    def __init__(self):
        self._progress = [' '] * 10

    def _print_progress(self, progress):
        self._progress[int(progress * 10)] = '#'
        print(''.join(self._progress))


if __name__ == '__main__':
    program = '+++>++[-<+>].'
    parser = FakeParser()
    compiler = Compiler(parser)
    progress = ProgressBar()
    progress.connect(compiler)
    print(compiler.compile(program))
