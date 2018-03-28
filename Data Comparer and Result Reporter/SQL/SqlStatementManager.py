
from DatabaseConfiguration import *

class SqlStatementManager:

        class SqlServer:
                @staticmethod
                def useDatabase(database):
                    return "use %s" % (database)

                @staticmethod
                def generateRowCountQueriesForAllTables():
                    return  "select \n" \
                            "case when row_number() over(order by name desc) = 1 \n" \
                            "then 'select '''+tab.name+''' TabName, count(*) as count from cdw.dbo.'+tab.name +' (readuncommitted)' \n" \
                            "else 'select '''+tab.name+''' TabName, count(*) as count from cdw.dbo.'+tab.name +' (readuncommitted)  union all' \n" \
                            "end \n" \
                            "from sysobjects tab \n" \
                            "where type = 'U' \n" \
                            "and uid = 1 \n" \
                            "order by name;"

                @staticmethod
                def getAllRowsFromTable(table):
                    return 'SELECT * FROM source.dbo.{}'.format(table)

                @staticmethod
                def getSchemaForTable(table):
                    return  "SELECT  c.name 'Column Name',t.Name 'Data type' " \
                            "FROM sys.columns c INNER JOIN sys.types t ON c.user_type_id = t.user_type_id " \
                            "LEFT OUTER JOIN sys.index_columns ic ON ic.object_id = c.object_id AND ic.column_id = c.column_id " \
                            "LEFT OUTER JOIN sys.indexes i ON ic.object_id = i.object_id AND ic.index_id = i.index_id " \
                            "WHERE c.object_id = OBJECT_ID('{}')".format(table)

                @staticmethod
                def getFullTableRowCount(table):
                        return "SELECT count(*) as Count FROM {}".format(table)

                @staticmethod
                def getIncrementalTableRowCount(table,uid,start,end):
                        return "select '{0}' as tablename, count(*) as count " \
                               "from {1}.dbo.{0} (readuncommitted) as a " \
                               "inner join {1}_stage.epic.{0}_Status as b (readuncommitted) " \
                               "on a.{2} = b.{2} " \
                               "where (lastupdateddate > '{3}' and lastupdateddate <= '{4}')".format(table,Database[:-1],uid,start,end)

                @staticmethod
                def getSampleTableData(table,ukey,uids):
                        return  'select * from {} (readuncommitted) ' \
                                'where {} in ({}) order by {}'.format(table,ukey,uids,ukey)

        class GoogleBigQuery:
                @staticmethod
                def getFullTableRowCount(table):
                        return "select '{2}', count(*) from `{0}.{1}.{2}`".format(Project, Dataset, table)

                @staticmethod
                def getFullDatasetTableNameAndRowCount(targetTablesString):
                        return 'SELECT _TABLE_SUFFIX AS table,count(*)as count FROM `{0}.{1}.*`\n' \
                                'where _TABLE_SUFFIX in ({2})\n' \
                                'group by _TABLE_SUFFIX\n' \
                                'order by _TABLE_SUFFIX'.format(Project,Dataset,targetTablesString)

                @staticmethod
                def getAllRowsFromTable(table):
                        return "SELECT * FROM `{0}.{1}.{2}` LIMIT 1000".format(Project, Dataset, table)

                @staticmethod
                def getSampleTableData(table):
                        #return "select * except(ExtractDate,LastUpdatedDate) from `{0}.{1}.{2}` order by rand() limit 100".format(Project,Dataset,table)
                        return "select * from `{0}.{1}.{2}` order by 1, rand() limit 100".format(Project, Dataset, table, id)
