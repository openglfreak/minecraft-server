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
        'minecraft-server-console.service'
        'minecraft-server-console.socket'
        'minecraft-server.service'
        'minecraft-server.socket'
        'minecraft-server-stdin.socket'
        'minecraft-server-stdout.socket'
        'minecraft-server-workaround-7069-before.service'
        'minecraft-server-workaround-7069-after.service'
        'player-count.py'
        'server-launch.sh'
        'socket-generator.sh')
sha256sums=('d3ba80c7706d83d25996a0072e426cbfdefe73d3557135c56c38c3124b4bb4db'
            'ddfcb64043c6e4ae44b7786ff7991ff71d56950d6d4d58b18bb9e716b4ce4b05'
            'b706e9e565426530473407c69111f02ce16c6b3e0072aef4dec1bbb6f7004201'
            '0eda1f642b5c3831ac387c5b51586f35ea33719e989f8db0b24f907eab2c5a80'
            'fde14d587117eb2523eb8902c28c2be0e71014171229a4370fb55658258cf24c'
            'a877ca48d2a01e225052d4a78d10b1ddb2bbf7c88e5204a563fabf64b3fd4b26'
            'c13ad562784d0b46de073d3397906d796b8709ad33ad6fdbac444a813af454e2'
            '6a23ab77b64667af3af4d16d4862f38ab7ac24eec93cd0b9616c3ea937f693eb'
            '691646fd25352552cf2f7c7d5479342d6e5d2ee9dec762e3e5cd0087483a36f2'
            '1928247b7f6e7046d764690db1465d443d74381681e1ee90b9a04a5a52471beb'
            'b06b50469036108945dc18012fb8a8048ebe6189fc883a3115ee799f275763ad'
            '2dff73d638ac2760f9aafc5fb402916a8e2fe92b1a485b65ad2710aa469aca8a'
            'eb251d96f88f58fef799e4e654f1f7c6750517d853cd545511a8fad26dcbab7f'
            'd17be777065c7cff9906b00c27e3f734c810f585cbf56206c65db6a116450964'
            'f567a6bb62ea4ef57360f532c3c93fa727615e831f401af005d37ecffaa0a1c0')

package() {
    install -Dm755 "${srcdir}/broadcast-socket.py" "${pkgdir}/usr/lib/minecraft-server/broadcast-socket.py"
    install -Dm755 "${srcdir}/console-connect.sh" "${pkgdir}/usr/bin/minecraft-server-console"
    install -Dm755 "${srcdir}/idle-stop.sh" "${pkgdir}/usr/lib/minecraft-server/idle-stop.sh"
    install -Dm644 "${srcdir}/minecraft-server.conf" "${pkgdir}/usr/lib/sysusers.d/minecraft-server.conf"
    install -Dm644 "${srcdir}/minecraft-server-console.service" "${pkgdir}/usr/lib/systemd/system/minecraft-server-console.service"
    install -Dm644 "${srcdir}/minecraft-server-console.socket" "${pkgdir}/usr/lib/systemd/system/minecraft-server-console.socket"
    install -Dm644 "${srcdir}/minecraft-server.service" "${pkgdir}/usr/lib/systemd/system/minecraft-server.service"
    install -Dm644 "${srcdir}/minecraft-server.socket" "${pkgdir}/usr/lib/systemd/system/minecraft-server.socket"
    install -Dm644 "${srcdir}/minecraft-server-stdin.socket" "${pkgdir}/usr/lib/systemd/system/minecraft-server-stdin.socket"
    install -Dm644 "${srcdir}/minecraft-server-stdout.socket" "${pkgdir}/usr/lib/systemd/system/minecraft-server-stdout.socket"
    install -Dm644 "${srcdir}/minecraft-server-workaround-7069-before.service" "${pkgdir}/usr/lib/systemd/system/minecraft-server-workaround-7069-before.service"
    install -Dm644 "${srcdir}/minecraft-server-workaround-7069-after.service" "${pkgdir}/usr/lib/systemd/system/minecraft-server-workaround-7069-after.service"
    install -Dm755 "${srcdir}/player-count.py" "${pkgdir}/usr/lib/minecraft-server/player-count.py"
    install -Dm755 "${srcdir}/server-launch.sh" "${pkgdir}/usr/lib/minecraft-server/server-launch.sh"
    install -Dm755 "${srcdir}/socket-generator.sh" "${pkgdir}/usr/lib/systemd/system-generators/minecraft-server-socket-generator.sh"
}
