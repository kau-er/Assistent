'''Тут слова на которые реагирует бот, что
обращение было к нему. Его имя и команда могут быть сказаны
в любой последовательности и даже в перемешку и тд...,
главное без продолжительной паузы'''

TRIGGERS = {'крендель','кренделек'}



'''Тренировочная модель для матрицы ИИ'''
data_set = {

'какая погода': 'weather сейчас скажу',
'какая погода на улице': 'weather боишься замерзнуть?',
'что там на улице': 'weather сейчас гляну...',
'сколько градусов': 'weather можешь выглянуть в окно, но сейчас проверю',
'запусти браузер': 'browser запускаю браузер',
'открой браузер': 'browser интернет активирован',
'интернет открой': 'browser открываю браузер',
'посмотреть фильм': 'browser сейчас открою браузер',
'играть': 'game лишь бы баловаться',
'хочу поиграть в игру': 'game а нам лишьбы баловаться',
'запусти игру': 'game запускаю игру, а нам лишь бы баловаться',
'выключи компьютер': 'offpc отключаю компьютер',
'отключись': 'offBot отключаюсь',
'как у тебя дела':'passive работаю в фоне, не переживай',
'что делаешь':'passive жду очередной команды, хоть мог бы и сам на кнопку нажать',
'привет':'passive и тебе привет',
'расскажи анекдот':'passive Вчера помыл окна, теперь у меня рассвет на два часа раньше...',
'работаешь':'passive как видишь',
'ты тут':'passive вроде да',
'что ты умеешь': 'passive я умею узнавать погоду, могу открыть браузер, запустить exe файл, выключить пк, отключиться, рассказать анекдот и еще тому чему ты меня научишь',
'справка': 'passive я умею узнавать погоду, могу открыть браузер, запустить exe файл, выключить пк, отключиться, рассказать анекдот и еще тому чему ты меня научишь',
}