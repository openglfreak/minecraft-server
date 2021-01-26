# Maintainer: Torge Matthies <openglfreak at googlemail dot com>

pkgname=minecraft-server
pkgver=1.0.2
pkgrel=1
pkgdesc="Minecraft server"
arch=('any')
license=('Boost')
depends=('java-runtime-headless' 'python' 'python-systemd')
optdepends=('socat: minecraft-server-console command')
source=('broadcast-socket.py'
        'console-connect.sh'
        'idle-stop.sh'
        'minecraft-server.conf'
        'minecraft-server-console@.service'
        'minecraft-server-console@.socket'
        'minecraft-server-idle-stop@.service'
        'minecraft-server-idle-stop@.timer'
        'minecraft-server@.service'
        'minecraft-server@.socket'
        'minecraft-server-stdin@.socket'
        'minecraft-server-stdout@.socket'
        'minecraft-server-workaround-7069-before@.service'
        'minecraft-server-workaround-7069-after@.service'
        'player-count.py'
        'server-launch.sh'
        'socket-generator.sh')
sha256sums=('6f3bd7223e467bf36bddf6abbedac1154310ebc4874cc790c1028f3a9f5b5323'
            '1e4fb847157a04b603b355d86e598c09c21d810a311eca91a95a4ce3e5a3ea9f'
            '7db5cd675e5ddbacdef762efac66a3d5a5ed11fe6b45a410a9b4f312fb616327'
            '25e955adbc09475626de0ab6cc2a95061fcad355b5e0585b7bec4b11ad05da37'
            '179de4e672791938fb424c7d53acf8b8d4b1d7be637d3e9be9c8e6ca38d81d30'
            '4aad7a71b53fd68ab1e9c32eb1452529f18d1f0e069a99ad1b136b3935cfa903'
            '06a949bf6954c3a567958d6ba72301637c185a804e04d1d21c7b2b5801ea2483'
            'a9cd444904d4297d010e3683968fea8409e3232d65c972ee2cbe73f3650fadb1'
            'ed7a520ffb4a9b744f5ccf17b3b034e10427805821aece534d2ad1624dad14c7'
            '4b53a2608eb7b93105d4a43bb9766ee37cdd5d9286b420becb6e9e8dd2243d99'
            'ac735089acb0a282ab5f356b4749fe83f1878c65e87a5cbf943e37208b47c1e5'
            'bf74b35ccd8f2ee4e9e93ef583e882fdb150956faf8f54d4e5b64587a440fb48'
            '70843061e04988809d0ca1074f10b416e7a1ff4d5b1fe42f6ecb6aed99d46566'
            '8ae1b982ee4aced56e1ab50160b4bc053f14417578ae69fab107803d10951840'
            '1163ba317b5c0f04301f153b986ebda94f41ec19fee23fb081305f7f0b9c3828'
            '56a746a6a6abd03b0338f5dade193788db7255f7f45cbf2ba206e7c616f9992b'
            'fda94e2338b32310411c21ecc1cbe5b27318865fd7d325e188d36648e670d2ba')

package() {
    install -Dm755 "${srcdir}/broadcast-socket.py" "${pkgdir}/usr/lib/minecraft-server/broadcast-socket.py"
    install -Dm755 "${srcdir}/console-connect.sh" "${pkgdir}/usr/bin/minecraft-server-console"
    install -Dm755 "${srcdir}/idle-stop.sh" "${pkgdir}/usr/lib/minecraft-server/idle-stop.sh"
    install -Dm644 "${srcdir}/minecraft-server.conf" "${pkgdir}/usr/lib/sysusers.d/minecraft-server.conf"
    install -Dm644 "${srcdir}/minecraft-server-console@.service" "${pkgdir}/usr/lib/systemd/system/minecraft-server-console@.service"
    install -Dm644 "${srcdir}/minecraft-server-console@.socket" "${pkgdir}/usr/lib/systemd/system/minecraft-server-console@.socket"
    install -Dm644 "${srcdir}/minecraft-server-idle-stop@.service" "${pkgdir}/usr/lib/systemd/system/minecraft-server-idle-stop@.service"
    install -Dm644 "${srcdir}/minecraft-server-idle-stop@.timer" "${pkgdir}/usr/lib/systemd/system/minecraft-server-idle-stop@.timer"
    install -Dm644 "${srcdir}/minecraft-server@.service" "${pkgdir}/usr/lib/systemd/system/minecraft-server@.service"
    install -Dm644 "${srcdir}/minecraft-server@.socket" "${pkgdir}/usr/lib/systemd/system/minecraft-server@.socket"
    install -Dm644 "${srcdir}/minecraft-server-stdin@.socket" "${pkgdir}/usr/lib/systemd/system/minecraft-server-stdin@.socket"
    install -Dm644 "${srcdir}/minecraft-server-stdout@.socket" "${pkgdir}/usr/lib/systemd/system/minecraft-server-stdout@.socket"
    install -Dm644 "${srcdir}/minecraft-server-workaround-7069-before@.service" "${pkgdir}/usr/lib/systemd/system/minecraft-server-workaround-7069-before@.service"
    install -Dm644 "${srcdir}/minecraft-server-workaround-7069-after@.service" "${pkgdir}/usr/lib/systemd/system/minecraft-server-workaround-7069-after@.service"
    install -Dm755 "${srcdir}/player-count.py" "${pkgdir}/usr/lib/minecraft-server/player-count.py"
    install -Dm755 "${srcdir}/server-launch.sh" "${pkgdir}/usr/lib/minecraft-server/server-launch.sh"
    install -Dm755 "${srcdir}/socket-generator.sh" "${pkgdir}/usr/lib/systemd/system-generators/minecraft-server-socket-generator.sh"
}
