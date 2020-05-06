from xml.dom import minidom
import xml.etree.ElementTree as ET
from urllib.request import urlopen
import ssl

class ochoquince():
    estadoConexion=False
    gw_addr="10.10.0.1"
    context = ssl._create_unverified_context() 

    def obtenerToken(self):
        gw_user="fibrastickets"
        gw_pass="s3aGD.4SFEdfW8E"
        url="https://" + self.gw_addr + ":815/gateway/integracion/login/?usuario=" + gw_user + "&password=" + gw_pass

        try:
            docXML= minidom.parse(urlopen(url, context=self.context))
            token815 = docXML.getElementsByTagName("token")[0]
            self.token = token815.firstChild.data
        except:
            self.token="Error al obtener token"   
        
        return self.token

    def obtenerPlanes(self,token):
        url="https://" + self.gw_addr + ":815/gateway/integracion/entrega/plan/listar/?token=" + token
        
        tree = ET.parse(urlopen(url, context=self.context))
        root = tree.getroot()

        listaPlanes = {}
        
        # f=0
        for elem in root:
            # listaplanes[f][0].append(elem.attrib.get("pk"))
            plan = elem.attrib.get("pk")
            for subelem in elem:

                if subelem.get('name')=="nombre":
                    # listaPlanes[f][1].append(subelem.text)
                    descripcion_plan = subelem.text
 
            listaPlanes[plan]=descripcion_plan

            # f=f+1
        return listaPlanes


    def obtenerClientes(self,token):
    
        planes = self.obtenerPlanes(token)
        
        url="https://" + self.gw_addr + ":815/gateway/integracion/clientes/cliente/listar/?token=" + token

        tree = ET.parse(urlopen(url, context=self.context))
        root = tree.getroot()

        listaClientes = []
        
        f=0
        for elem in root:
            listaClientes.append([])
            
            listaClientes[f].append(elem.attrib.get("pk")) 

            for subelem in elem:

                if subelem.get('name')=="nombre": # Indice 0
                    listaClientes[f].append(subelem.text)

                if subelem.get('name')=="domicilio": # Indice 1
                    listaClientes[f].append(subelem.text)

                if subelem.get('name')=="activo": # Indice 2
                    listaClientes[f].append(subelem.text)

                # if subelem.get('name')=="plan": # Incide 3
                #     plan = planes[subelem.text]
                #     listaClientes[f].append(plan)

                try:
                    if subelem.get('name')=="conector": # Indice 4
                        listaClientes[f].append(subelem.text)
                except:
                    listaClientes[f].append(str("No establecido"))


            f=f+1
        return listaClientes

    def obtenerConexiones(self,token):
        
        planes = self.obtenerPlanes(token)
        
        url="https://" + self.gw_addr + ":815/gateway/integracion/clientes/cuentasimple/listar/?token=" + token
        #url="https://" + self.gw_addr + ":815/gateway/integracion/clientes/cliente/listar/?token=" + token

        tree = ET.parse(urlopen(url, context=self.context))
        root = tree.getroot()

        listaClientes = []
        
        f=0
        for elem in root:
            listaClientes.append([])
            
            listaClientes[f].append(elem.attrib.get("pk")) 

            for subelem in elem:

                if subelem.get('name')=="nombre": # Indice 0
                    listaClientes[f].append(subelem.text)

                if subelem.get('name')=="domicilio": # Indice 1
                    listaClientes[f].append(subelem.text)

                if subelem.get('name')=="activa": # Indice 2
                    listaClientes[f].append(subelem.text)

                if subelem.get('name')=="plan": # Incide 3
                    plan = planes[subelem.text]
                    listaClientes[f].append(plan)

                try:
                    if subelem.get('name')=="conector": # Indice 4
                        listaClientes[f].append(subelem.text)
                except:
                    listaClientes[f].append(str("No establecido"))


            f=f+1
        return listaClientes
