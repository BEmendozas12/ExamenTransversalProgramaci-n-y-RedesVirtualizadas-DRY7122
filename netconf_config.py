from ncclient import manager

# Conexión al router usando NETCONF
conexion = manager.connect(
    host="192.168.56.101",  # IP del router
    port=830,               # Puerto NETCONF por defecto
    username="cisco",
    password="cisco",
    hostkey_verify=False
)

# Cambiar el nombre del router (hostname)
nuevo_hostname = """
<config>
  <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
    <hostname>Morales-Espinoza-Mateluna-Mendoza</hostname>
  </native>
</config>
"""
conexion.edit_config(target='running', config=nuevo_hostname)

# Crear interfaz loopback 111 con IP 111.111.111.111/32
loopback_111 = """
<config>
  <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
    <interface>
      <Loopback>
        <name>111</name>
        <ip>
          <address>
            <primary>
              <address>111.111.111.111</address>
              <mask>255.255.255.255</mask>
            </primary>
          </address>
        </ip>
      </Loopback>
    </interface>
  </native>
</config>
"""
conexion.edit_config(target='running', config=loopback_111)

print("Configuración aplicada exitosamente.")
conexion.close_session()
