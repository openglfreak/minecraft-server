# Maintainer: Torge Matthies <openglfreak at googlemail dot com>

pkgname=minecraft-server
pkgver=0.1.0
pkgrel=1
pkgdesc="Minecraft server"
arch=('x86_64')
license=('proprietary')
depends=('java-runtime' 'python' 'python-systemd' 'socat')
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
sha256sums=('d3ba80c7706d83d25996a0072e426cbfdefe73d3557135c56c38c3124b4bb4db'
            '63154941c49c4728657e93a70f71b884c85038e02ee98086189462e6ed0a3cb5'
            '1525996c1bdd30dbc92984efbef0791d0ecdbdfe265659c242300161caf508c8'
            '0eda1f642b5c3831ac387c5b51586f35ea33719e989f8db0b24f907eab2c5a80'
            '4e4aa95b4205759a0646996c9662d1b5fb035aaf651371e7ab9b0d84b5e2509e'
            '1f23059d5658d02a6b45e5d4a030293e8d68020f238ffa1feac502b4869654d7'
            'c3d481369739bcd57690f5d13acce68be058984c41ab7a251aabd222060d926f'
            '7759c1d94e499638dcd48d55da82c4741d4f9a2f3bf5933eab3f40301ba735d7'
            '25a2a41e5a9bda420301b50d0c78097595dcae209ab358851fae2a96fa38afb2'
            'ebe4ef12281214dab141540ecc6e86add9e16ecfcf4a1f1ba2dd52d71c6c40d3'
            '89fdee21397f0805ff821dbad8f1c81305332ac2319ffa9f59376134599e01b7'
            '45704053d032f488ffb31242b2dc4775414418fcc9f7c82907e2ae1efaec8276'
            '74e5562163b760059f13a94c3a274ad2c6a7fea342177e55ec244e549d13e7ac'
            'be3e112c5069eda5ac56caf21b1d534da44af2966e23fee9172716c7d28c0094'
            '60c8c05788240096c8c0068ba8e171ebee7fd9f360f421c42587c81bff1d0339'
            'd17be777065c7cff9906b00c27e3f734c810f585cbf56206c65db6a116450964'
            '31467f738dc150e78c39d7a8d8f2812dba2e39cbcafe3bf6faa5278016c05529')

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
