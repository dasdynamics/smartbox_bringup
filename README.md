# `smartbox_bringup`

ROS 2-пакет для запуска основных компонентов робота **SmartBox**.

## Описание

Пакет содержит общий launch-файл, который параллельно запускает launch-файлы других пакетов, необходимых для работы робота.

В текущей версии пакет объединяет следующие компоненты:

- пакет симуляции `dasdynamics_simulation`;
- пакет навигации `dasdynamics_navigation`;
- пакет голосового управления `dasdynamics_voice`.

Таким образом, `smartbox_bringup` служит единой точкой запуска всей системы SmartBox.

## Зависимости

Перед сборкой `smartbox_bringup` необходимо скачать и собрать зависимые пакеты.

### Пакет симуляции

```bash
git clone https://github.com/dasdynamics/dasdynamics_simulation.git
```

### Пакет навигации

```bash
git clone https://github.com/dasdynamics/dasdynamics_navigation.git
```

### Пакет голосового управления

```bash
git clone https://github.com/dasdynamics/dasdynamics_voice.git
```

Поместите все репозитории в каталог `src` одного рабочего пространства ROS 2.

Например:

```text
ros2_ws/
└── src/
    ├── smartbox_bringup/
    ├── dasdynamics_simulation/
    ├── dasdynamics_navigation/
    └── dasdynamics_voice/
```

После добавления пакетов установите зависимости и выполните сборку рабочего пространства:

```bash
cd ~/ros2_ws
colcon build
source install/setup.bash
```

Путь `~/ros2_ws` необходимо заменить на путь к вашему рабочему пространству.

## Требования

Для работы пакета требуется:

- установленный ROS 2;
- собранные пакеты `dasdynamics_simulation`, `dasdynamics_navigation` и `dasdynamics_voice`;
- корректно настроенные зависимости этих пакетов;
- активированное рабочее пространство ROS 2.

Перед запуском выполните:

```bash
source /opt/ros/<ROS_DISTRO>/setup.bash
source ~/ros2_ws/install/setup.bash
```

Вместо `<ROS_DISTRO>` укажите имя установленного дистрибутива ROS 2.

## Быстрый запуск

После сборки рабочего пространства запустите общий launch-файл:

```bash
ros2 launch smartbox_bringup bringup.launch.py
```

Этот файл запускает компоненты симуляции, навигации и голосового управления роботом.

## Настройка

Основной файл запуска находится в каталоге `launch`:

```text
launch/bringup.launch.py
```

Если требуется изменить порядок запуска, параметры компонентов или список подключаемых пакетов, отредактируйте этот файл.

При изменении имён пакетов, launch-файлов или конфигураций проверьте соответствующие параметры и пути в `bringup.launch.py`.

## Структура репозитория

```text
launch/
    bringup.launch.py    — общий файл запуска системы SmartBox
```

## Новости разработки

Последние новости о разработке проекта публикуются в группе ВКонтакте:

- **ВКонтакте:** [ДАС Динамика](https://vk.ru/dasdynamics)

## Контакты

Если у вас остались вопросы, вы можете связаться по следующим контактам:

- **Почта:** [das-dev-md@mail.com](mailto:das-dev-md@mail.com)
- **Telegram:** [@das_dev_tg](https://t.me/das_dev_tg)
