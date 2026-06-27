interface DashboardCardProps {
  title: string;
  value: string | number;
  description?: string;
}

export default function DashboardCard({
  title,
  value,
  description,
}: DashboardCardProps) {
  return (
    <div className="bg-white dark:bg-gray-800 shadow-lg rounded-xl p-6 border border-gray-200 dark:border-gray-700 transition-all hover:shadow-xl">
      
      <h3 className="text-sm font-medium text-gray-500 dark:text-gray-400">
        {title}
      </h3>

      <div className="mt-2 text-3xl font-bold text-gray-900 dark:text-white">
        {value}
      </div>

      {description && (
        <p className="mt-2 text-sm text-gray-500 dark:text-gray-400">
          {description}
        </p>
      )}
    </div>
  );
}