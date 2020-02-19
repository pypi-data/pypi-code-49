from iocbio.kinetics.handler.experiment_generic import ExperimentGeneric
from iocbio.kinetics.constants import database_table_experiment

IocbioKineticsModule = ["database_schema"]


class ExperimentTutorial(ExperimentGeneric):

    database_table = "tutorial_data"
    
    @staticmethod
    def database_schema(db):
        db.query("CREATE TABLE IF NOT EXISTS " + db.table(ExperimentTutorial.database_table) +
                 "(experiment_id text PRIMARY KEY, rawdata text, filename text, title text, " +
                 "FOREIGN KEY (experiment_id) REFERENCES " + db.table(database_table_experiment) + "(experiment_id) ON DELETE CASCADE" +
                 ")")
    
    @staticmethod
    def get_fulltxt(database, experiment_id):
        # check if the record with the experiment_id exists and reflects our hardware
        if ExperimentGeneric.hardware(database, experiment_id) != 'tutorial_hardware':
            return None
        print('Loading raw data for experiment:', experiment_id)
        # read in the raw text
        for q in database.query("SELECT rawdata FROM " + database.table(ExperimentTutorial.database_table) +
                                " WHERE experiment_id=:experiment_id",
                                experiment_id=experiment_id):
            return q.rawdata
        return None

    @staticmethod
    def store(database, data, fulltxt):
        experiment_id = data.experiment_id

        # store reference to the experiment in generic table
        ExperimentGeneric.store(database, experiment_id, time=data.time,
                                type_generic=data.type_generic,
                                type_specific=data.type, hardware="tutorial_hardware")

        c = database
        
        if not database.has_record(ExperimentTutorial.database_table,
                                   experiment_id = experiment_id):
           c.query("INSERT INTO " + database.table(ExperimentTutorial.database_table) +
                   "(experiment_id, rawdata, filename, title) " +
                   "VALUES(:experiment_id,:ftxt,:fname,:exptitle)",
                   experiment_id=experiment_id,
                   ftxt=fulltxt,
                   fname=data.config["this_file"],
                   exptitle=data.config["Experiment name"])

# definition of database_schema function
def database_schema(db):
    # just in case if our experiment is the first one, make general if needed
    ExperimentGeneric.database_schema(db)
    # create table for our experiment
    ExperimentTutorial.database_schema(db)
