import os

from bgmi.config import (
    BGMI_PATH, FRONT_STATIC_PATH, IS_WINDOWS, SAVE_PATH, SCRIPT_PATH, TMP_PATH, TOOLS_PATH
)
from bgmi.utils import exec_command, print_error, print_info, print_success, print_warning


def install_crontab() -> None:
    if os.getenv('BGMI_IN_DOCKER'):
        print_warning('env BGMI_IN_DOCKER exists, skip install crontab')
        return
    print_info('Installing crontab job')
    if IS_WINDOWS:
        base = os.path.join(os.path.dirname(__file__), 'others\\windows\\cron')
        exec_command(
            'SCHTASKS /Create /TN "bgmi calendar updater" /SC HOURLY /MO 2 '
            '/TR "{tr}" /F'.format(tr=os.path.join(base, 'cal.vbs'))
        )

        exec_command(
            'SCHTASKS /Create /TN "bgmi bangumi updater" /SC HOURLY /MO 12 '
            '/TR "{tr}" /F'.format(tr=os.path.join(base, 'update.vbs'))
        )
    else:
        path = os.path.join(os.path.dirname(__file__), 'others/crontab.sh')
        exec_command("bash '%s'" % path)


def create_dir() -> None:
    path_to_create = (BGMI_PATH, SAVE_PATH, TMP_PATH, SCRIPT_PATH, TOOLS_PATH, FRONT_STATIC_PATH)

    if not os.environ.get('HOME', os.environ.get('USERPROFILE', None)):
        print_warning('$HOME and $BGMI_PATH not set, use a tmp dir ' + BGMI_PATH)

    # bgmi home dir
    try:
        for path in path_to_create:
            if not os.path.exists(path):
                os.makedirs(path)
                print_success('%s created successfully' % path)
    except OSError as e:
        print_error('Error: {}'.format(str(e)))
