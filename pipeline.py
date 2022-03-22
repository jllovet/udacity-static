from diagrams import Cluster, Diagram, Edge
from diagrams.aws.compute import EC2
from diagrams.aws.storage import S3
from diagrams.onprem.vcs import Github
from diagrams.onprem.ci import Jenkins
from diagrams.onprem.client import User

with Diagram(show=False, filename="jenkins_s3_static_cicd", direction="LR", outformat="png", graph_attr={"pad": "1", "fontsize": "25"}):
    with Cluster("Pipeline"):
        u = User() 
        gh = Github()
        j = Jenkins()
        s3 = S3()

        u >> Edge(label="Commit pushed") >> gh
        gh >> Edge(label="Pull from Jenkins") >> j
        j >> Edge(label="Publish if build succeeds") >> s3