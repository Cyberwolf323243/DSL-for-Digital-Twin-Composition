using System.Threading.Tasks;

namespace SampleClientApp
{
    public class BuildingScenario
    {
        private readonly CommandLoop cl;
        public BuildingScenario(CommandLoop cl)
        {
            this.cl = cl;
        }

        public async Task InitBuilding()
        {
            Log.Alert($"Deleting all twins...");
            await cl.DeleteAllTwinsAsync();
            Log.Out($"Creating 1 Car and 1 electrical Engine...");
            await InitializeGraph();
        }

        private async Task InitializeGraph()
        {
            string[] modelsToUpload = new string[3] {"CreateModels", "Car", "ElectricEngine" };
            Log.Out($"Uploading {string.Join(", ", modelsToUpload)} models");

            await cl.CommandCreateModels(modelsToUpload);

            Log.Out($"Creating Car and Engine...");
            await cl.CommandCreateDigitalTwin(new string[6]
                {
                    "CreateTwin", "dtmi:example:Car;1", "car",
                    "DisplayName", "string", "Car"
                });
            await cl.CommandCreateDigitalTwin(new string[15]
                {
                    "CreateTwin", "dtmi:example:ElectricalEngine;1", "engine",
                    "RPM", "double", "0",
                    "Utilization", "double", "0",
                    "PowerConsumption", "double", "0",
                    "PowerSavingMode", "boolean", "false"
                });

            Log.Out($"Creating edges between the Car and the electrical Engine");
            await cl.CommandCreateRelationship(new string[5]
                {
                    "CreateEdge", "car", "contains", "engine", "car_to_engine_edge"
                });
        }
    }
}
