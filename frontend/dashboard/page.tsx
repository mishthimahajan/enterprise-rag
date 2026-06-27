import DashboardCard
from "@/components/DashboardCard";

export default function Dashboard() {

  return (

    <div className="grid grid-cols-4 gap-4 p-6">

      <DashboardCard
        title="Documents"
        value="152"
      />

      <DashboardCard
        title="Queries"
        value="3200"
      />

      <DashboardCard
        title="Users"
        value="24"
      />

      <DashboardCard
        title="Accuracy"
        value="94%"
      />

    </div>

  );
}