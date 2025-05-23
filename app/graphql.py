import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from app.models import Bank, Branch
from datetime import datetime, timedelta

class BankType(SQLAlchemyObjectType):
    class Meta:
        model = Bank
        interfaces = (graphene.relay.Node,)

class BranchType(SQLAlchemyObjectType):
    class Meta:
        model = Branch
        interfaces = (graphene.relay.Node,)

class Query(graphene.ObjectType):
    node = graphene.relay.Node.Field()
    
    branches = SQLAlchemyConnectionField(
        BranchType,
        hours=graphene.Int(description="Filter branches updated in the last N hours")
    )
    
    banks = SQLAlchemyConnectionField(BankType)

    def resolve_branches(self, info, hours=None, **kwargs):
        query = Branch.query
        
        if hours is not None:
            time_threshold = datetime.utcnow() - timedelta(hours=hours)
            query = query.filter(Branch.updated_at >= time_threshold)
            
        return query

schema = graphene.Schema(query=Query) 