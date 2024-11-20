import io
import json
import logging
import oci
from fdk import response


def handler(ctx, data: io.BytesIO = None):
        config = {}
        body = json.loads(data.getvalue())
        #set the region where you want to auth
        config["region"] = body["region"]
        signer = oci.auth.signers.get_resource_principals_signer()
        compute_cl = oci.core.ComputeClient(config=config, signer=signer)
        list_instances_response = compute_cl.list_instances(compartment_id="ocid1.compartment...........")
        return list_instances_response.data[0].availability_domain


####


francisc_v@cloudshell:hello (eu-frankfurt-1)$ echo -n '{"region": "us-ashburn-1"}' | fn invoke fvass-test-app hello
GqIF:US-ASHBURN-AD-2
francisc_v@cloudshell:hello (eu-frankfurt-1)$ echo -n '{"region": "us-phoenix-1"}' | fn invoke fvass-test-app hello
GqIF:PHX-AD-3
francisc_v@cloudshell:hello (eu-frankfurt-1)$ echo -n '{"region": "eu-frankfurt-1"}' | fn invoke fvass-test-app hello
GqIF:EU-FRANKFURT-1-AD-1
francisc_v@cloudshell:hello (eu-frankfurt-1)$ 